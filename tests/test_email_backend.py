import pytest
from django.core.mail import EmailMessage

from smtp2go_django.email_backend import (
    Smtp2goAPIContentException,
    Smtp2goEmailBackend,
)


@pytest.fixture
def test_messages():
    return [
    EmailMessage(
        subject='Test Message',
        body='Test Message Text',
        from_email='dave@example.com',
        to=['matt@example.com']
    ),
    EmailMessage(
        subject='Test Message 2',
        body='Test Message 2 Text',
        from_email='dave@example.com',
        to=['matt@example.com']
    )
]
TEST_API_KEY = 'testapikey'


def test_missing_to_field(monkeypatch, test_messages):
    monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    email_backend = Smtp2goEmailBackend()
    for message in test_messages:
        setattr(message, 'to', None)
    # assert not any([getattr(message, 'to', None) message in test_messages])
    with pytest.raises(Smtp2goAPIContentException):
        email_backend.send_messages(test_messages)


# def test_missing_from_email_field(monkeypatch, test_messages):
#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend()
#     for message in test_messages:
#         setattr(message, 'from', None)
#     assert not any([message.from for message in test_messages])
#     with pytest.raises(Smtp2goAPIContentException):
#         email_backend.send_messages(test_messages)

#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend()
#     setattr(test_messages[0], 'from_email', None)
#     with pytest.raises(Smtp2goAPIContentException):
#         email_backend.send_messages(test_messages)
#
#
# def test_missing_subject_field(monkeypatch, test_messages):
#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend()
#     setattr(test_messages[0], 'subject', None)
#     with pytest.raises(Smtp2goAPIContentException):
#         email_backend.send_messages(test_messages)
#
#
# def test_missing_body_field(monkeypatch, test_messages):
#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend()
#     setattr(test_messages[0], 'body', None)
#     with pytest.raises(Smtp2goAPIContentException):
#         email_backend.send_messages(test_messages)
#
#
# def test_fail_silently_supresses_errors(monkeypatch, test_messages):
#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend(fail_silently=True)
#     setattr(test_messages[0], 'body', None)
#     email_backend.send_messages(test_messages)
#
#
# def test_successfully_sent_count(monkeypatch, test_messages):
#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend()
#     monkeypatch.setattr(email_backend, '_smtp2go_send', lambda x: None)
#     assert email_backend.send_messages(test_messages) == len(test_messages)
#
#
# def test_successfully_sent_multiple_messages_count(monkeypatch, test_messages):
#     multiplier = 10
#     t = test_messages * multiplier
#     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
#     email_backend = Smtp2goEmailBackend()
#     monkeypatch.setattr(email_backend, '_smtp2go_send', lambda x: None)
#     assert email_backend.send_messages(t) == multiplier
