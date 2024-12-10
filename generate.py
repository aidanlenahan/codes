import os
import smtplib
import datetime
import random
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Email configuration from environment variables
SMTP_SERVER = os.getenv("SMTP_SERVER")  # SMTP server address
SMTP_PORT = int(os.getenv("SMTP_PORT", 587))  # SMTP server port (default 587 for TLS)
EMAIL_ADDRESS = os.getenv("EMAIL_ADDRESS")  # Email address for sending
EMAIL_PASSWORD = os.getenv("EMAIL_PASSWORD")  # Password or app password

# Family email addresses from environment variables
FAMILY_EMAIL_1 = os.getenv("FAMILY_EMAIL_1")
FAMILY_EMAIL_2 = os.getenv("FAMILY_EMAIL_2")
FAMILY_EMAIL_3 = os.getenv("FAMILY_EMAIL_3")
FAMILY_EMAIL_4 = os.getenv("FAMILY_EMAIL_4")

family_emails = [FAMILY_EMAIL_1, FAMILY_EMAIL_2, FAMILY_EMAIL_3, FAMILY_EMAIL_4]

# List of words/phrases
words = [
    "Sunshine", "Moonlight", "Starlight", "Ocean Breeze", 
    "Mountain Peak", "Golden Hour", "Snowfall", "Rainy Day", 
    "Crimson Sky", "Emerald Forest", "Lighthouse", "Sandy Beach",
    "Twilight Glow", "Amber Horizon", "Forest Whisper", "Silent Echo", 
    "Crystal Waters", "Azure Skies", "Morning Dew", "Autumn Leaves",
    "Blazing Fire", "Frosty Chill", "Velvet Night", "Radiant Glow",
    "Whispering Pines", "Serene Meadow", "Starry Night", "Gentle Breeze",
    "Horizon Glow", "Deep Ocean", "Cobalt Mist", "Dusky Dunes",
    "Evergreen Dreams", "Golden Sands", "Icy Rivers", "Summer Bliss",
    "Crescent Moon", "Shimmering Stars", "Eternal Flame", "Echoing Valley",
    "Misty Mountains", "Amber Fields", "Flowing River", "Velvet Clouds",
    "Silver Lining", "Jade Reflection", "Whistling Winds", "Frozen Tundra",
    "Vivid Sunset", "Windswept Prairie", "Golden Glow", "Crystalline Snow",
    "Ocean's Embrace", "Rustling Leaves", "Calm Waters", "Quiet Streams",
    "Autumn Glow", "Shadowed Peaks", "Luminous Sky", "Vibrant Horizon"
]

def get_weekly_code():
    # Get the current week number of the year
    week_number = datetime.date.today().isocalendar()[1]
    random.seed(week_number)
    return random.choice(words)

def send_email(code):
    # Create the email
    subject = f"Code of Week {datetime.date.today().isocalendar()[1]} - {datetime.date.today().strftime('%B %Y')}"
    body = f"Hello Family,\n\nThis week's code is: {code}\n\nStay safe!"
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the email server and send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            for recipient in family_emails:
                if recipient:  # Only send to valid emails
                    msg['To'] = recipient
                    server.sendmail(EMAIL_ADDRESS, recipient, msg.as_string())
        print("Emails sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Generate the code and send the email
if __name__ == "__main__":
    weekly_code = get_weekly_code()
    send_email(weekly_code)
