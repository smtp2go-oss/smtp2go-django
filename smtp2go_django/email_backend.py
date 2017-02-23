from threading import RLock
from smtplib import SMTPException
from ssl import SSLError

from django.core.mail.backends.base import BaseEmailBackend

from smtp2go.core import SMTP2Go
from smtp2go.exceptions import SMTP2GoBaseException

from inspect import getargspec


class SMTP2GoAPIContentException(SMTP2GoBaseException):
    pass


class SMTP2GoEmailBackend(BaseEmailBackend):
    """
    SMTP2Go wrapper for Django's Email Backend
    """
    def __init__(self, fail_silently=False, **kwargs):
        super(SMTP2GoEmailBackend, self).__init__(fail_silently=fail_silently)
        # Django's EmailMessage parameters:
        self.email_message_parameters = ['from_email', 'to', 'subject', 'body']
        # smtp2go-python parameters:
        self.required_params = ['sender', 'recipients', 'subject', 'message']
        self.lock = RLock()

    def _get_payload(self, email_message):
        """
        Extracts parameters from Django's EmailMessage object.
        Raises SMTP2GoAPIContentException if a required parameter is missing
        Raised exceptions may be supressed by calling function - contingent on
        self.fail_silently

        Returns dict contraining SMTP2Go parameters:
        {'sender': u'goofy@clubhouse.com',
         'recipients': ['mickey@clubhouse.com'],
         'subject': u'Trying out SMTP2Go',
         'message': u'Test Message'}
        """
        # Get content from EmailMessage:
        email_content = [getattr(
            email_message, p) for p in self.email_message_parameters]
        payload = dict(zip(self.required_params, email_content))
        # Raise exception if any parameters are missing:
        if not all(payload.values()):
            raise SMTP2GoAPIContentException(
                'The following parameters are required: {0}'.format(
                    self.required_params))
        return payload

    def send_messages(self, email_messages):
        """
        Wraps SMTP2Go Python API library
        """
        lock = RLock()
        with lock:
            sent_count = 0
            for message in email_messages:
                try:
                    payload = self._get_payload(message)
                    s = SMTP2Go()
                    s.send(**payload)
                    sent_count += 1
                except (SMTPException, SSLError, SMTP2GoBaseException):
                    if not self.fail_silently:
                        raise
        return sent_count
