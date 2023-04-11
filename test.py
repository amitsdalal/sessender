import os
from sessender import SesSender

def test_send_email():
    # Set environment variables
    os.environ['SES_USERNAME'] = 'your_ses_user'
    os.environ['SES_PASS'] = 'your_ses_password'
    os.environ['SES_HOST'] = 'email-smtp.ap-south-1.amazonaws.com'
    os.environ['SES_PORT'] = '587'
    os.environ['EMAIL_RECIPIENT'] = 'recipient@example.com'
    os.environ['EMAIL_SENDER'] = ''

    # Create a SesSender instance
    sender = SesSender()

    # Send a plain text email
    sender.send_email(
        subject='Test Plain Text Email',
        message='This is a test plain text email.'
    )

    # Send an HTML email
    sender.send_email(
        subject='Test HTML Email',
        html_message='<h1>This is a test HTML email.</h1>'
    )

    # Send an email with an attachment
    sender.send_email(
        subject='Test Email with Attachment',
        message='This is a test email with an attachment.',
        attachment='LICENSE'
    )

    # Send an email with multiple recipients, CC, and BCC
    sender.send_email(
        subject='Test Email with Multiple Recipients, CC, and BCC',
        message='This is a test email with multiple recipients, CC, and BCC.',
        sender='ad@example.com',
        recipients=['ad@example.com', 'ad+test@example.com'],
        cc=['ad+cc1@example.com', 'ad+cc2@example.com'],
        bcc=['ad+bcc1@example.com', 'ad+bcc2@example.com']
    )

    print("All test cases passed!")

test_send_email()
