import resend
from app.core.config import get_settings

settings = get_settings()
resend.api_key = settings.RESEND_API_KEY


def send_reset_email(recipient_email: str, reset_link: str):
    try:
        resend.Emails.send({
            "from": "AI Hiring System <onboarding@resend.dev>",
            "to": [recipient_email],
            "subject": "Reset Your Password",
            "html": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #8b5cf6;">AI Hiring System</h2>
                    <p>Hello,</p>
                    <p>We received a request to reset your password.</p>
                    <p>
                        <a href="{reset_link}"
                           style="background:#8b5cf6;color:white;padding:12px 24px;
                                  border-radius:8px;text-decoration:none;display:inline-block;">
                            Reset My Password
                        </a>
                    </p>
                    <p>This link will expire in <strong>1 hour</strong>.</p>
                    <p>If you did not request this, you can safely ignore this email.</p>
                    <hr/>
                    <small style="color:#94a3b8;">AI Hiring System · Powered by AI</small>
                </div>
            """
        })
    except Exception as e:
        print(f"Email send error: {str(e)}")


def send_admin_email(recipient_email: str, subject: str, message_body: str):
    try:
        resend.Emails.send({
            "from": "AI Hiring System <onboarding@resend.dev>",
            "to": [recipient_email],
            "subject": subject,
            "html": f"""
                <div style="font-family: Arial, sans-serif; max-width: 600px; margin: 0 auto;">
                    <h2 style="color: #8b5cf6;">AI Hiring System</h2>
                    <div style="background:#f8fafc;padding:20px;border-radius:8px;
                                border-left:4px solid #8b5cf6;">
                        {message_body}
                    </div>
                    <hr/>
                    <small style="color:#94a3b8;">AI Hiring System · Powered by AI</small>
                </div>
            """
        })
    except Exception as e:
        print(f"Email send error: {str(e)}")