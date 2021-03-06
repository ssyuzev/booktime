"""Tests for forms."""

from django.test import TestCase
from django.core import mail
from .. import forms


class TestForm(TestCase):
    """Test bundle for main app forms."""

    def test_valid_contact_us_forms_sends_email(self):
        """Test valid contact us form send email."""
        form = forms.ContactForm({
            "name": "Luke Skywalker",
            "message": "Hi there",
        })
        self.assertTrue(form.is_valid())

        with self.assertLogs('main.forms', level="INFO") as cm:
            form.send_mail()

        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, "Site message")

        self.assertGreaterEqual(len(cm.output), 1)

    def test_invalid_contact_us_form(self):
        """Test invalid contact us form."""
        form = forms.ContactForm({'message': "Hi there"})
        self.assertFalse(form.is_valid())
