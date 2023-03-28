# Sessender

Sessender is a Python package for sending emails using Amazon SES. It provides a simple interface for sending plain text and HTML emails, as well as attachments.

## Installation

You can install Sessender using pip:

```
pip install sessender
```


## Usage
-----

To use Sessender, you need to provide your Amazon SES credentials as environment variables:

- `SES_USERNAME`: Your Amazon SES SMTP username.
- `SES_PASS`: Your Amazon SES SMTP password.
- `SES_HOST`: Your Amazon SES SMTP host.
- `SES_PORT`: Your Amazon SES SMTP port.
- `EMAIL_RECIPIENT`: The recipient email address.
- `EMAIL_SENDER`: The sender email address.


Then, create a `Sessender` object with your credentials:

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

## Contributing
If you'd like to contribute to Sessender, please fork the repository and create a pull request. We welcome contributions of all kinds, including bug fixes, new features, and documentation improvements.

# License
Sessender is licensed under the MIT License. See LICENSE for more information.