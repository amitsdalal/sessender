# Sessender

Sessender is a Python package for sending emails using Amazon SES. It provides a simple interface for sending plain text and HTML emails, as well as attachments.

## Installation

You can install Sessender using pip:

```
pip install sessender
```



## Usage

To use Sessender, you need to provide your Amazon SES credentials as environment variables:

- `SES_USERNAME`: Your Amazon SES SMTP username.
- `SES_PASS`: Your Amazon SES SMTP password.
- `SES_HOST`: Your Amazon SES SMTP host.
- `SES_PORT`: Your Amazon SES SMTP port.
- `EMAIL_RECIPIENT`: The recipient email address (optional, can be set when calling `send_email`).
- `EMAIL_SENDER`: The sender email address (optional, can be set when calling `send_email`).

Then, create a `SesSender` object with your credentials:

```python
from sessender import SesSender

sender = SesSender()


sender.send_email(
    subject='Hello, world!',
    message='This is a test email from Sessender.',
)

```
You can also include attachments with your emails by passing a file path to the attachment parameter:

```python
sender.send_email(
    subject='Hello, world!',
    message='This is a test email from Sessender with an attachment.',
    attachment='/path/to/attachment.txt'
)
```
To send a html email, use the send_email method with the html_message parameter:

```python
sender.send_email(
    subject='Hello, world!',
    html_message='<h1>This is a test email from Sessender in HTML format.</h1>',
)
```
You can also include attachments with your emails by passing a file path to the attachment parameter:

```python
sender.send_email(
    subject='Hello, world!',
    html_message='This is a test email from Sessender with an attachment.',
    attachment='/path/to/attachment.txt'
)
```


### `send_email` method parameters
This example demonstrates the usage of all the parameters available in the `send_email` method.


- `subject` (required): A string representing the subject of the email.
- `message` (optional): A string containing the plain text content of the email. Use either `message` or `html_message`, but not both.
- `html_message` (optional): A string containing the HTML content of the email. Use either `message` or `html_message`, but not both.
- `attachment` (optional): A file path to the attachment you want to include in the email. The attachment should be readable by the script.
- `sender` (optional): A string representing the sender's email address. If not provided, the sender will be read from the `EMAIL_SENDER` environment variable.
- `recipients` (optional): A list of strings representing the recipient email addresses. If not provided, the recipient will be read from the `EMAIL_RECIPIENT` environment variable.
- `cc` (optional): A list of strings representing the CC (Carbon Copy) email addresses.
- `bcc` (optional): A list of strings representing the BCC (Blind Carbon Copy) email addresses.

Example usage:

```python
sender.send_email(
    subject='Hello, world!',
    message='This is a test email from Sessender.',
    recipients=['recipient1@example.com', 'recipient2@example.com'],
    sender='sender@example.com',
    cc=['cc1@example.com', 'cc2@example.com'],
    bcc=['bcc1@example.com', 'bcc2@example.com'],
    attachment='/path/to/attachment.txt'
)
```

## Contributing
If you'd like to contribute to Sessender, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

# License
Sessender is licensed under the MIT License. See LICENSE for more information.