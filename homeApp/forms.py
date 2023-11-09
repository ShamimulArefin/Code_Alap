from django import forms
from homeApp.models import Contact, MailList


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = "__all__"

class MailListForm(forms.ModelForm):
    class Meta:
        model = MailList
        fields = "__all__"