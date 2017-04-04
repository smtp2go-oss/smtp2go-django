import pytest

from smtp2go_django.email_backend import (
    Smtp2goEmailBackend,
    Smtp2goAPIContentException,
)


class TestEmailBackend:

    def test_sends_email_successfully(self, email_backend, test_message):
        email_backend.send_messages([test_message])

    def test_send_messages_requires_iterable(
            self, email_backend, test_message):
        with pytest.raises(TypeError):
            email_backend.send_messages(test_message)

    @pytest.mark.parametrize('field', ['to', 'from_email', 'subject', 'body'])
    def test_send_email_with_missing_field(
            self, field, email_backend, test_message):
        # Utility function to attempt to send an email with a missing field:
        setattr(test_message, field, None)
        assert not getattr(test_message, field)
        with pytest.raises(Smtp2goAPIContentException):
            email_backend.send_messages([test_message])

    def test_successfully_sent_single_message_count(
            self, monkeypatch, email_backend, test_message):
        single_message_iterable = [test_message]
        count = len(single_message_iterable)
        assert email_backend.send_messages(single_message_iterable) == count

    def test_successfully_sent_multiple_messages_count(
            self, monkeypatch, email_backend, test_message):
        count = 10
        messages = [test_message for i in range(count)]
        assert email_backend.send_messages(messages) == count

    def test_fail_silently_supresses_errors(monkeypatch, test_message):
        email_backend = Smtp2goEmailBackend(fail_silently=True)
        setattr(test_message, 'to', None)
        email_backend.send_messages([test_message])
