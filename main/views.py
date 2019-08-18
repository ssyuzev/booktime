"""Views for main app."""

from django.views.generic.edit import FormView
from . import forms


class ContactUsView(FormView):
    """View for contact us form."""

    template_name = "contact_form.html"
    form_class = forms.ContactForm
    success_url = "/"

    def form_valid(self, form):
        """Send mail if form is valid."""
        form.send_mail()
        return super().form_valid(form)
