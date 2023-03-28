try:
    import os
    import traceback
    import logging
    import smtplib
    from email.mime.multipart import MIMEMultipart
    from email.mime.text import MIMEText
    from email.mime.application import MIMEApplication
except ImportError as e:
    raise e

class SesSender:
    def __init__(self):
        try:
            self.smtp_username = os.getenv('SES_USERNAME')
            self.smtp_password = os.getenv('SES_PASS')
            self.smtp_host = os.getenv('SES_HOST')
            self.smtp_port = os.getenv('SES_PORT')
            self.recipient = os.getenv('EMAIL_RECIPIENT')
            self.sender = os.getenv('EMAIL_SENDER')

            # Configure logging
            logging.basicConfig(filename='seslog.txt', level=logging.DEBUG, format='%(asctime)s - %(levelname)s - %(message)s')

        except Exception as e:
            error_msg = f"Error initializing Sessender:\n{traceback.format_exc()}"
            print(error_msg)
            logging.error(error_msg)
            raise e

    def send_email(self, subject, message, attachment=None):
        try:
            # Create a message
            msg = MIMEMultipart()
            msg['From'] = self.sender
            msg['To'] = self.recipient
            msg['Subject'] = subject
            msg.attach(MIMEText(message))

            # Add attachment to message if specified
            if attachment:
                with open(attachment, 'rb') as f:
                    part = MIMEApplication(f.read(), Name=os.path.basename(attachment))
                    part['Content-Disposition'] = f'attachment; filename="{os.path.basename(attachment)}"'
                    msg.attach(part)

            # Connect to the SMTP server and send the message
            with smtplib.SMTP(self.smtp_host, int(self.smtp_port)) as smtp:
                smtp.starttls()
                smtp.login(self.smtp_username, self.smtp_password)
                smtp.sendmail(self.sender, self.recipient, msg.as_string())

            # Log success
            logging.info(f"Email sent: {subject}")

        except:
            # Log error
            error_msg = f"Error sending email:\n{traceback.format_exc()}"
            logging.error(error_msg)
            print(error_msg)
