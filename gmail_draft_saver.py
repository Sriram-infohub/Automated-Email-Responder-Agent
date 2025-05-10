import base64
from email.mime.text import MIMEText
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

SCOPES = ['https://www.googleapis.com/auth/gmail.compose']

def authenticate_gmail():
    flow = InstalledAppFlow.from_client_secrets_file('credentials.json', SCOPES)
    creds = flow.run_local_server(port=0)
    return build('gmail', 'v1', credentials=creds)

def create_draft(service, user_id, message_body, subject, to_email):
    message = MIMEText(message_body)
    message['to'] = to_email
    message['subject'] = subject
    raw_message = base64.urlsafe_b64encode(message.as_bytes()).decode()

    draft = {
        'message': {
            'raw': raw_message
        }
    }

    return service.users().drafts().create(userId=user_id, body=draft).execute()

# Usage
if __name__ == '__main__':
    service = authenticate_gmail()
    create_draft(
        service,
        'me',
        message_body="Here is your draft response.",
        subject="RE: Your Subject",
        to_email="recipient@example.com"
    )
