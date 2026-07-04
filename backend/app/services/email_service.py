import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from app.core.config import get_settings

settings = get_settings()


def send_email(recipient_email: str, subject: str, html_body: str):
    try:
        msg = MIMEMultipart("alternative")
        msg["Subject"] = subject
        msg["From"] = f"AI Hiring System <{settings.ADMIN_EMAIL}>"
        msg["To"] = recipient_email

        msg.attach(MIMEText(html_body, "html"))

        with smtplib.SMTP(settings.SMTP_SERVER, settings.SMTP_PORT) as server:
            server.ehlo()
            server.starttls()
            server.login(settings.ADMIN_EMAIL, settings.ADMIN_EMAIL_PASSWORD)
            server.sendmail(settings.ADMIN_EMAIL, recipient_email, msg.as_string())

        print(f"Email sent successfully to {recipient_email}")

    except Exception as e:
        print(f"Email send error: {str(e)}")
        raise Exception(f"Failed to send email: {str(e)}")


def send_reset_email(recipient_email: str, reset_link: str):
    html = f"""
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
    send_email(recipient_email, "Reset Your Password", html)


def send_admin_email(recipient_email: str, subject: str, message_body: str):
    html = f"""
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
    send_email(recipient_email, subject, html)