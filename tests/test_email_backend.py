from django.core.mail import EmailMessage
import pytest
import responses

from smtp2go_django.email_backend import SMTP2GoEmailBackend

TEST_API_KEY = 'testapikey'
TEST_MESSAGES = [EmailMessage(
    subject='Test Message',
    body='Test!',
    from_email='test@test.com',
    to=['testers@test.com']
)]

def _mock_endpoint():
    # Mock out API Endpoint:
    http_return_code = 200
    responses.add(responses.POST, API_ROOT + ENDPOINT_SEND,
                  json=SUCCESSFUL_RESPONSE, status=http_return_code,
                  content_type='application/json')


def test_send(monkeypatch):
    monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    s = SMTP2GoEmailBackend()
    sent_count = s.send_messages(TEST_MESSAGES)
    assert sent_count == len(TEST_MESSAGES)
