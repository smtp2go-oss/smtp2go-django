import pytest
import responses
from django.core.mail import EmailMessage
from smtp2go.settings import API_ROOT, ENDPOINT_SEND

from smtp2go_django.email_backend import SMTP2GoEmailBackend, SMTP2GoAPIContentException

TEST_API_KEY = 'testapikey'


@pytest.fixture
def TEST_MESSAGES():
    return [EmailMessage(
        subject='Test Message',
        body='Test!',
        from_email='test@test.com',
        to=['testers@test.com']
    )]


def test_missing_to_field(monkeypatch, TEST_MESSAGES):
    monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    email_backend = SMTP2GoEmailBackend()
    setattr(TEST_MESSAGES[0], 'to', None)
    with pytest.raises(SMTP2GoAPIContentException):
        email_backend.send_messages(TEST_MESSAGES)

def test_missing_from_email_field(monkeypatch, TEST_MESSAGES):
    monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    email_backend = SMTP2GoEmailBackend()
    setattr(TEST_MESSAGES[0], 'from_email', None)
    with pytest.raises(SMTP2GoAPIContentException):
        email_backend.send_messages(TEST_MESSAGES)

def test_missing_subject_field(monkeypatch, TEST_MESSAGES):
    monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    email_backend = SMTP2GoEmailBackend()
    setattr(TEST_MESSAGES[0], 'subject', None)
    with pytest.raises(SMTP2GoAPIContentException):
        email_backend.send_messages(TEST_MESSAGES)

def test_missing_body_field(monkeypatch, TEST_MESSAGES):
    monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    email_backend = SMTP2GoEmailBackend()
    setattr(TEST_MESSAGES[0], 'body', None)
    with pytest.raises(SMTP2GoAPIContentException):
        email_backend.send_messages(TEST_MESSAGES)
