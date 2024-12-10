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
        "Morning Horizon", "Serene Twilight", "Golden Twilight", "Crystal Shoreline", 
    "Cobalt Lagoon", "Mountain Song", "Ethereal Mist", "Radiant Shores", 
    "Echoing Waves", "Hidden Lagoon", "Amber Twilight", "Mystic Forest", 
    "Sunlit Horizon", "Azure Tide", "Sapphire Bloom", "Gilded Dawn", 
    "Emerald Haven", "Frosted Pines", "Velvet Shadows", "Misty Dawn", 
    "Lush Canopy", "Snowy Peaks", "Autumn Chill", "Radiant Peaks", 
    "Dappled Sunlight", "Golden Horizon", "Sandy Cove", "Shimmering Dew", 
    "Starfall Night", "Gentle Ripple", "Twilight Horizon", "Luminous Peaks", 
    "Rustic Meadow", "Breezy Coast", "Silver Horizon", "Dusky Plains", 
    "Ethereal Waves", "Crescent Reflection", "Morning Glow", "Crimson Horizon", 
    "Silent Woods", "Crystal Glow", "Shining Shores", "Winter Radiance", 
    "Deep Reflection", "Golden Dunes", "Summer Horizon", "Dewy Fields", 
    "Starry Plains", "Frosty Peaks", "Lush Horizon", "Evening Radiance", 
    "Ocean Melody", "Forest Dreams", "Eternal Horizon", "Breezy Valley", 
    "Winter Dreams", "Silver Reflections", "Misty Echo", "Golden Fields", 
    "Shadowed Horizon", "Rustling Breeze", "Cobalt Reflections", "Frozen Horizon", 
    "Vivid Reflections", "Horizon Whispers", "Crimson Sunset", "Dusk Glow", 
    "Sapphire Horizon", "Autumn Reflections", "Ocean Glow", "Radiant Reflections", 
    "Frozen Reflection", "Shimmering Horizon", "Sunset Radiance", "Twilight Echoes", 
    "Amber Morning", "Luminous Shadows", "Velvet Glow", "Silent Radiance", 
    "Winter Bliss", "Gilded Reflections", "Snowy Echoes", "Crystal Horizon", 
    "Autumn Whispers", "Golden Waves", "Serene Reflections", "Misty Radiance", 
    "Frosty Dreams", "Radiant Glow", "Rustic Reflections", "Horizon Echoes", 
    "Sapphire Glow", "Amber Reflections", "Shadowed Dreams", "Starry Radiance", 
    "Ocean Reflections", "Evening Whispers", "Autumn Glow", "Golden Radiance", 
    "Silver Glow", "Misty Horizon", "Dappled Radiance", "Frosty Shores", 
    "Snowy Reflection", "Luminous Radiance", "Cobalt Shadows", "Velvet Dreams", 
    "Morning Reflections", "Amber Glow", "Ethereal Radiance", "Silent Horizon", 
    "Golden Bliss", "Frozen Radiance", "Shimmering Reflections", "Twilight Bliss", 
    "Rustling Shadows", "Crystal Reflections", "Sunset Whispers", "Winter Glow", 
    "Autumn Dreams", "Golden Shadows", "Snowy Whispers", "Serene Radiance", 
    "Ocean Dreams", "Eternal Radiance", "Amber Bliss", "Silver Dreams", 
    "Horizon Dreams", "Twilight Radiance", "Cobalt Dreams", "Misty Whispers", 
    "Rustic Whispers", "Golden Dreams", "Starry Whispers", "Snowy Dreams", 
    "Silver Radiance", "Velvet Whispers", "Winter Radiance", "Shimmering Dreams", 
    "Frozen Bliss", "Sunlit Reflections", "Autumn Bliss", "Ethereal Glow", 
    "Golden Bliss", "Crystal Dreams", "Ocean Whispers", "Serene Dreams", 
    "Golden Horizon", "Morning Whispers", "Lush Reflections", "Frosty Radiance", 
    "Shimmering Whispers", "Frozen Radiance", "Amber Whispers", "Sapphire Whispers", 
    "Golden Reflections", "Velvet Reflections", "Ethereal Horizon", "Dewy Glow", 
    "Crystal Whispers", "Radiant Horizon", "Autumn Bliss", "Snowy Bliss", 
    "Starry Dreams", "Frozen Dreams", "Shimmering Radiance", "Twilight Dreams", 
    "Golden Whispers", "Amber Radiance", "Sapphire Radiance", "Crescent Dreams", 
    "Velvet Radiance", "Serene Horizon", "Luminous Whispers", "Shimmering Echoes", 
    "Autumn Radiance", "Misty Dreams", "Crystal Bliss", "Golden Echoes", 
    "Winter Bliss", "Amber Echoes", "Rustic Bliss", "Velvet Echoes", 
    "Dappled Bliss", "Sunlit Radiance", "Ocean Bliss", "Silver Echoes", 
    "Crescent Radiance", "Rustling Radiance", "Snowy Radiance", "Shimmering Shadows", 
    "Winter Whispers", "Golden Shadows", "Serene Shadows", "Crystal Shadows", 
    "Autumn Echoes", "Amber Glow", "Sapphire Echoes", "Ethereal Whispers", 
    "Frosty Whispers", "Velvet Glow", "Radiant Whispers", "Frozen Whispers", 
    "Silver Whispers", "Dappled Radiance", "Golden Glow", "Starry Echoes", 
    "Ocean Radiance", "Shimmering Glow", "Amber Shadows", "Velvet Reflections", 
    "Twilight Shadows", "Golden Echoes", "Sunlit Glow", "Silver Glow", 
    "Winter Shadows", "Crystal Glow", "Frozen Shadows", "Golden Radiance", 
    "Amber Bliss", "Velvet Dreams", "Twilight Echoes", "Ocean Glow", 
    "Crescent Glow", "Eternal Bliss", "Golden Bliss", "Morning Glow", 
    "Luminous Echoes", "Rustling Glow", "Autumn Shadows", "Silver Shadows", 
    "Sapphire Bliss", "Radiant Shadows", "Shimmering Bliss", "Frozen Bliss", 
    "Winter Glow", "Crystal Bliss", "Amber Glow", "Starry Bliss", 
    "Golden Shadows", "Silver Bliss", "Ocean Shadows", "Dewy Shadows", 
    "Velvet Bliss", "Radiant Bliss", "Frozen Radiance", "Twilight Shadows", 
    "Luminous Radiance", "Rustling Radiance", "Serene Radiance", "Misty Bliss", 
    "Ethereal Bliss", "Amber Radiance", "Golden Reflections", "Snowy Bliss", 
    "Starry Shadows", "Ocean Echoes", "Frozen Reflections", "Amber Echoes", 
    "Shimmering Reflections", "Velvet Radiance", "Twilight Reflections", "Morning Bliss"
]

def get_weekly_code():
    # Get the current week number of the year
    week_number = datetime.date.today().isocalendar()[1]
    random.seed(week_number)
    return random.choice(words)

def send_email(code):
    # Create the email
    subject = f"Code of Week {datetime.date.today().isocalendar()[1]} - {datetime.date.today().strftime('%B %Y')}"
    body = f"Hello Family,\n\nThis week's code is: {code}\n\n\nDISCLAIMERS:\n\nThis is an automated email sent every Monday at 6:20AM (EST). The sender address, f3fff0@gmail.com, is a noreply.\n\nThe content of this email is confidential and intended for the recipient specified in message only. It is strictly forbidden to share any part of this message with any third party, without a written consent of the sender."
    msg = MIMEMultipart()
    msg['From'] = EMAIL_ADDRESS
    msg['To'] = ", ".join([email for email in family_emails if email])  # Combine all recipients
    msg['Subject'] = subject
    msg.attach(MIMEText(body, 'plain'))

    # Connect to the email server and send the email
    try:
        with smtplib.SMTP(SMTP_SERVER, SMTP_PORT) as server:
            server.starttls()  # Secure the connection
            server.login(EMAIL_ADDRESS, EMAIL_PASSWORD)
            server.sendmail(EMAIL_ADDRESS, family_emails, msg.as_string())  # Send to all recipients
        print("Emails sent successfully!")
    except Exception as e:
        print(f"Error sending email: {e}")

# Generate the code and send the email
if __name__ == "__main__":
    weekly_code = get_weekly_code()
    # pass weekly code into send_email
    send_email(weekly_code)
