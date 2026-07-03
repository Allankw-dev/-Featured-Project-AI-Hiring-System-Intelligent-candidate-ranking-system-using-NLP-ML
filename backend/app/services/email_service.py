import resend
from app.core.config import get_settings

settings = get_settings()
resend.api_key = settings.RESEND_API_KEY


def send_reset_email(recipient_email: str, reset_link: str):
    resend.Emails.send({
        "from": "AI Hiring System <onboarding@resend.dev>",  # or your verified domain
        "to": [recipient_email],
        "subject": "Reset Your Password",
        "html": f"""
            <p>Hello,</p>
            <p>We received a request to reset your password.</p>
            <p><a href="{reset_link}">Click here to reset it</a></p>
            <p>This link will expire in 1 hour.</p>
            <p>If you did not request this, you can safely ignore this email.</p>
        """
    })
def send_admin_email(subject: str, message: str, recipient_email: str = None):
    """
    Send a notification email to the admin.
    If recipient_email is not provided, falls back to settings.ADMIN_EMAIL.
    """
    to_address = recipient_email or settings.ADMIN_EMAIL

    resend.Emails.send({
        "from": "AI Hiring System <onboarding@resend.dev>",  # or your verified domain
        "to": [to_address],
        "subject": subject,
        "html": f"""
            <p>{message}</p>
        """
    })