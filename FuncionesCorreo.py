import base64
from email.mime.audio import MIMEAudio
from email.mime.base import MIMEBase
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import mimetypes
import os
import json

class Correo():
    def __init__(self, service):
        self.service = service
        self.Draft = None

    def Create_Message(self, sender, to, subject, message_text):
        message = MIMEText(message_text)
        message['to'] = to
        message['from'] = sender
        message['subject'] = subject
        raw = base64.urlsafe_b64encode(message.as_bytes())
        raw = raw.decode()
        body = {'raw': raw}
        return body

    def Create_Draft(self, user_id, message_body):
        try:
            message = {'message': message_body}
            # message = json.dumps(message)
            self.Draft = self.service.users().drafts().create(userId=user_id, body=message).execute()

            print('Draft id: '+self.Draft['id']+'\nDraft message: '+self.Draft['message'])

            return self.Draft
        except Exception as e:
            print('An error occurred: '+str(e))
            return None