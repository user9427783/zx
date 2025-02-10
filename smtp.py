import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
import mimetypes

# Input details
receiver = input("Enter the receiver email id: ")


# Normalize file path (replace backslashes with forward slashes or use raw string)
file_path = "C:\\Users\\bncoe\\OneDrive\\Desktop\\Omkar.pdf"
# Create SMTP session
obj = smtplib.SMTP("smtp.gmail.com", 587)
obj.ehlo()
obj.starttls()

# Login using the App Password
obj.login("greenify9427783@gmail.com", "bejn nlrx hdgb vlao")

# Prepare the email content
subject = "Subject: 1st program of Internship"
body = "Hi This Is My First Program."
# Create the MIME object
msg = MIMEMultipart()
msg['From'] = "greenify9427783@gmail.com"
msg['To'] = receiver
msg['Subject'] = subject

# Attach the body message
msg.attach(MIMEText(body, 'plain'))

# Determine the MIME type of the file
mime_type, encoding = mimetypes.guess_type(file_path)
if mime_type is None:
    mime_type = 'application/octet-stream'  # Default MIME type if unknown

# Attach the file
try:
    with open(file_path, "rb") as attachment:
        part = MIMEBase(mime_type.split('/')[0], mime_type.split('/')[1])
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header(
            "Content-Disposition",
            f"attachment; filename={file_path.split('/')[-1]}"
        )
        msg.attach(part)
except Exception as e:
    print(f"Error attaching file: {e}")

# Send the email
obj.sendmail("greenify9427783@gmail.com", receiver, msg.as_string())

# Quit the SMTP session
obj.quit()

print(f"File path used: {file_path}")
