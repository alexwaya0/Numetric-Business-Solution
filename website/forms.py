from django import forms

from .models import Service


class ContactForm(forms.Form):

    full_name = forms.CharField(
        max_length=150,
        label="Full Name",
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your full name",
                "autocomplete": "name",
            }
        ),
    )

    company_name = forms.CharField(
        max_length=150,
        label="Company Name",
        required=False,
        widget=forms.TextInput(
            attrs={
                "placeholder": "Your company name",
                "autocomplete": "organization",
            }
        ),
    )

    email = forms.EmailField(
        label="Email",
        widget=forms.EmailInput(
            attrs={
                "placeholder": "you@company.com",
                "autocomplete": "email",
            }
        ),
    )

    phone = forms.CharField(
        max_length=30,
        label="Phone",
        widget=forms.TextInput(
            attrs={
                "placeholder": "+254 7XX XXX XXX",
                "autocomplete": "tel",
            }
        ),
    )

    service = forms.ModelChoiceField(
        queryset=Service.objects.filter(
            is_active=True
        ),
        label="Service Required",
        empty_label="Select a service",
        widget=forms.Select(),
    )

    message = forms.CharField(
        label="Message",
        min_length=10,
        widget=forms.Textarea(
            attrs={
                "placeholder": "Tell us briefly how we can help...",
                "rows": 6,
            }
        ),
    )

    def clean_phone(self):

        phone = self.cleaned_data["phone"].strip()

        allowed = set(
            "0123456789+()- "
        )

        if not all(
            character in allowed
            for character in phone
        ):
            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        return phone