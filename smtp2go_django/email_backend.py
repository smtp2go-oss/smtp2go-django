from threading import RLock
from smtplib import SMTPException
from ssl import SSLError

from django.core.mail.backends.base import BaseEmailBackend

from smtp2go.core import Smtp2goClient
from smtp2go.exceptions import Smtp2goBaseException


class Smtp2goAPIContentException(Smtp2goBaseException):
    pass


class Smtp2goEmailBackend(BaseEmailBackend):
    """
    smtp2go wrapper for Django's Email Backend
    """
    def __init__(self, fail_silently=False, **kwargs):
        super(Smtp2goEmailBackend, self).__init__(fail_silently=fail_silently)
        self.smtp2go = Smtp2goClient()
        self.lock = RLock()

    def _get_payload(self, email_message):
        """
        Extracts parameters from Django's EmailMessage object.
        Raises Smtp2goAPIContentException if a required parameter is missing
        Raised exceptions may be supressed by calling function - contingent on
        self.fail_silently

        Returns dict containing smtp2go parameters:
        {'sender': u'dave@example.com',
         'recipients': ['matt@example.com'],
         'subject': u'Trying out smtp2go',
         'message': u'Test Message'}
        """
        # Get content from EmailMessage:
        payload = {
            'sender': getattr(email_message, 'from_email', None),
            'recipients': getattr(email_message, 'to', None),
            'subject': getattr(email_message, 'subject', None),
        }
        text = getattr(email_message, 'body', None)
        html = self._get_html(email_message)

        # Raise exception if any parameters are missing and fail_silently=False:
        if not all(payload.values()) or not any([text, html]):
            if not self.fail_silently:
                raise Smtp2goAPIContentException(
                    'The following parameters are required: {0} '
                    'and one or both of text or html'.format(
                        payload.keys()))
        payload['text'], payload['html'] = text, html
        return payload

    def _get_html(self, email_message):
        alternatives, html = getattr(email_message, 'alternatives', None), None
        if alternatives:
            try:
                html, __ = alternatives[0]
            except (IndexError, ValueError):
                pass
        return html

    def _smtp2go_send(self, payload):
        self.smtp2go.send(**payload)

    def send_messages(self, email_messages):
        """
        Wraps smtp2go Python API library
        """
        with self.lock:
            sent_count = 0
            for message in email_messages:
                try:
                    payload = self._get_payload(message)
                    self._smtp2go_send(payload)
                    sent_count += 1
                except (SMTPException, SSLError, Smtp2goBaseException):
                    if not self.fail_silently:
                        raise
        return sent_count
