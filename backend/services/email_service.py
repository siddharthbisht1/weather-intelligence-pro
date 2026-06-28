import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart

from backend.config import (
    EMAIL_HOST,
    EMAIL_PORT,
    EMAIL_ADDRESS,
    EMAIL_PASSWORD
)


# ==========================================
# Send Email
# ==========================================

def send_email(receiver_email: str, subject: str, body: str):
    try:
        message = MIMEMultipart()
        message["From"] = EMAIL_ADDRESS
        message["To"] = receiver_email
        message["Subject"] = subject

        message.attach(MIMEText(body, "plain"))

        server = smtplib.SMTP(EMAIL_HOST, EMAIL_PORT)
        server.starttls()
        server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
        
        server.sendmail(
            EMAIL_ADDRESS,
            receiver_email,
            message.as_string()
        )
        server.quit()

        return {
            "message": "Email sent successfully"
        }

    except Exception as e:
        return {
            "error": str(e)
        }


# ==========================================
# Welcome Email
# ==========================================

def send_welcome_email(receiver_email: str, username: str):
    subject = "Welcome to Weather Intelligence Pro"

    body = f"""Hello {username},

Welcome to Weather Intelligence Pro.
Your account has been created successfully.

Enjoy AI-powered weather forecasts,
AQI analytics, water quality monitoring,
and intelligent insights.

Regards,
Weather Intelligence Pro Team
"""

    return send_email(receiver_email, subject, body)


# ==========================================
# Password Reset Email
# ==========================================

def send_password_reset_email(receiver_email: str, reset_link: str):
    subject = "Password Reset Request"

    body = f"""Click the link below to reset your password:

{reset_link}

If you didn't request this, please ignore this email.
"""

    return send_email(receiver_email, subject, body)


# ==========================================
# Weather Alert Email
# ==========================================

def send_weather_alert(receiver_email: str, city: str):
    subject = "Weather Alert"

    body = f"""Important weather update for {city}.

Please check your dashboard for the latest information.
"""

    return send_email(receiver_email, subject, body)


# ==========================================
# AQI Alert Email
# ==========================================

def send_aqi_alert(receiver_email: str, city: str):
    subject = "AQI Alert"

    body = f"""Air quality has deteriorated in {city}.

Please take precautions.
"""

    return send_email(receiver_email, subject, body)