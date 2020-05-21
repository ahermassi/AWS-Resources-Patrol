def verify_sender(sender, ses):
    print('Verifying sender email address')
    ses.verify_email_identity(EmailAddress=sender)
    print('Sender email address verified. Check your inbox.')
