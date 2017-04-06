import pytest

from django.core.mail import EmailMessage, EmailMultiAlternatives
from smtp2go_django.email_backend import Smtp2goEmailBackend


@pytest.fixture(autouse=True)
def set_env(monkeypatch):
    # Set API key for Smtp2goClient::
    test_api_key = 'testapikey'
    monkeypatch.setenv('SMTP2GO_API_KEY', test_api_key)


@pytest.fixture(autouse=True)
def email_backend(set_env):
    return Smtp2goEmailBackend()


@pytest.fixture(autouse=True)
def disallow_external_requests(monkeypatch, email_backend):
    # assert False, 'BUTTFERZZZ!'
    monkeypatch.setattr(email_backend, '_smtp2go_send', lambda x: None)


@pytest.fixture()
def test_message(autouse=True):
    return EmailMessage(
        subject='Test Message',
        body='Test Message Text',
        from_email='dave@example.com',
        to=['matt@example.com']
    )

@pytest.fixture()
def test_multipart_message(autouse=True):
    payload = {
        'to': ['matt@example.com'],
        'from_email': 'dave@example.com',
        'subject': 'Test Message',
        'body': 'Test Message Text'
    }
    html_content = '<html><body><h1>Test Message HTML</h1></body></html>'
    message = EmailMultiAlternatives(**payload)
    message.attach_alternative(html_content, "text/html")
    return message
