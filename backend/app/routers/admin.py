from fastapi import APIRouter, Depends, HTTPException, BackgroundTasks, Request
from sqlalchemy.orm import Session
from slowapi import Limiter
from slowapi.util import get_remote_address

from app.core.dep import get_db, require_admin
from app.models.application import Application
from app.models.user import User
from app.models.job import Job
from app.models.email_log import EmailLog
from app.services.email_service import send_admin_email
from app.schemas.admin import CandidateEmailRequest

router = APIRouter(prefix="/admin", tags=["Admin"])
limiter = Limiter(key_func=get_remote_address)


@router.get("/top-candidates")
@limiter.limit("30/minute")
def top_candidates(
    request: Request,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    rows = (
        db.query(Application, User, Job)
        .join(User, Application.user_id == User.id)
        .join(Job, Application.job_id == Job.id)
        .order_by(Application.overall_score.desc())
        .limit(20)
        .all()
    )

    results = []
    for app_row, user, job in rows:
        results.append({
            "application_id": app_row.id,
            "applicant_name": user.full_name,
            "applicant_email": user.email,
            "job_title": job.title,
            "company": job.company,
            "overall_score": app_row.overall_score,
            "semantic_score": app_row.semantic_score,
            "skills_score": app_row.skills_score,
            "experience_score": app_row.experience_score,
            "verification_score": app_row.verification_score,
            "status": app_row.status
        })
    return results


@router.post("/applications/{application_id}/shortlist")
@limiter.limit("20/minute")
def shortlist_candidate(
    request: Request,
    application_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    application.status = "shortlisted"
    db.commit()
    return {"message": "Candidate shortlisted successfully"}


@router.post("/applications/{application_id}/reject")
@limiter.limit("20/minute")
def reject_candidate(
    request: Request,
    application_id: int,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    application = db.query(Application).filter(Application.id == application_id).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")
    application.status = "rejected"
    db.commit()
    return {"message": "Candidate rejected successfully"}


@router.post("/send-email")
@limiter.limit("10/minute")
def send_email_to_candidate(
    request: Request,
    payload: CandidateEmailRequest,
    background_tasks: BackgroundTasks,
    db: Session = Depends(get_db),
    current_user=Depends(require_admin)
):
    application = db.query(Application).filter(
        Application.id == payload.application_id
    ).first()
    if not application:
        raise HTTPException(status_code=404, detail="Application not found")

    user = db.query(User).filter(User.id == application.user_id).first()
    if not user:
        raise HTTPException(status_code=404, detail="User not found")

    background_tasks.add_task(
        send_admin_email,
        recipient_email=user.email,
        subject=payload.subject,
        message_body=payload.message_body
    )

    log = EmailLog(
        application_id=application.id,
        recipient_email=user.email,
        subject=payload.subject,
        message_body=payload.message_body,
        sent_by=current_user.id
    )
    db.add(log)
    db.commit()

    return {"message": f"Email sent successfully to {user.email}"}