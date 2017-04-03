import pytest
from django.core.mail import EmailMessage

from smtp2go.exceptions import Smtp2goParameterException
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


class TestEmailBackend:
    def test_missing_to_field(self, monkeypatch, test_messages):
        monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
        email_backend = Smtp2goEmailBackend()
        for message in test_messages:
            setattr(message, 'to', None)
        assert not any([getattr(message, 'to', None) for message in test_messages])
        with pytest.raises(Smtp2goAPIContentException):
            email_backend.send_messages(test_messages)


    def test_missing_from_email_field(self, monkeypatch, test_messages):
        monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
        email_backend = Smtp2goEmailBackend()
        for message in test_messages:
            setattr(message, 'from_email', None)
        assert not any([message.from_email for message in test_messages])
        with pytest.raises(Smtp2goAPIContentException):
            email_backend.send_messages(test_messages)


    def test_missing_subject_field(self, monkeypatch, test_messages):
        monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
        email_backend = Smtp2goEmailBackend()
        for message in test_messages:
            setattr(message, 'subject', None)
        assert not any([message.subject for message in test_messages])
        with pytest.raises(Smtp2goAPIContentException):
            email_backend.send_messages(test_messages)


    def test_missing_body_field(self, monkeypatch, test_messages):
        monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
        email_backend = Smtp2goEmailBackend()
        for message in test_messages:
            setattr(message, 'body', None)
        assert not any([message.body for message in test_messages])
        # TODO: Unify exceptions
        with pytest.raises(Smtp2goParameterException):
            email_backend.send_messages(test_messages)
    #
    # def test_successfully_sent_count(self, monkeypatch, test_messages):
    #     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    #     email_backend = Smtp2goEmailBackend()
    #     monkeypatch.setattr(email_backend, '_smtp2go_send', lambda x: None)
    #     assert email_backend.send_messages(test_messages) == len(test_messages)
    #
    #
    # # TODO: Mock request
    # # def test_fail_silently_supresses_errors(monkeypatch, test_messages):
    # #     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    # #     email_backend = Smtp2goEmailBackend(fail_silently=True)
    # #     setattr(test_messages[0], 'body', None)
    # #     email_backend.send_messages(test_messages)
    # #
    # #
    # def test_successfully_sent_multiple_messages_count(self, monkeypatch, test_messages):
    #     multiplier = 10
    #     t = test_messages * multiplier
    #     monkeypatch.setenv('SMTP2GO_API_KEY', TEST_API_KEY)
    #     email_backend = Smtp2goEmailBackend()
    #     monkeypatch.setattr(email_backend, '_smtp2go_send', lambda x: None)
    #     assert email_backend.send_messages(t) == multiplier
