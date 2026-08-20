import re

from django import forms

from .models import Service


# ==========================================================
# CONTACT FORM
# ==========================================================

class ContactForm(forms.Form):

    # ======================================================
    # FULL NAME
    # ======================================================

    full_name = forms.CharField(
        max_length=150,
        min_length=2,
        label="Full Name",
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Your full name",
                "autocomplete": "name",
                "required": True,
            }
        ),
    )


    # ======================================================
    # COMPANY NAME
    # ======================================================

    company_name = forms.CharField(
        max_length=200,
        label="Company Name",
        required=False,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "Your company name",
                "autocomplete": "organization",
            }
        ),
    )


    # ======================================================
    # EMAIL ADDRESS
    # ======================================================

    email = forms.EmailField(
        max_length=254,
        label="Email Address",
        required=True,
        widget=forms.EmailInput(
            attrs={
                "class": "form-input",
                "placeholder": "you@company.com",
                "autocomplete": "email",
                "inputmode": "email",
                "required": True,
            }
        ),
    )


    # ======================================================
    # PHONE NUMBER
    # ======================================================

    phone = forms.CharField(
        max_length=30,
        min_length=7,
        label="Phone Number",
        required=True,
        strip=True,
        widget=forms.TextInput(
            attrs={
                "class": "form-input",
                "placeholder": "+254 7XX XXX XXX",
                "autocomplete": "tel",
                "inputmode": "tel",
                "required": True,
            }
        ),
    )


    # ======================================================
    # SERVICE REQUIRED
    # ======================================================

    service = forms.ModelChoiceField(
        queryset=Service.objects.none(),
        label="Service Required",
        required=True,
        empty_label="Select a service",
        widget=forms.Select(
            attrs={
                "class": "form-select",
                "required": True,
            }
        ),
    )


    # ======================================================
    # MESSAGE
    # ======================================================

    message = forms.CharField(
        max_length=5000,
        min_length=10,
        label="Message",
        required=True,
        strip=True,
        widget=forms.Textarea(
            attrs={
                "class": "form-textarea",
                "placeholder": (
                    "Tell us briefly how we can help "
                    "your business..."
                ),
                "rows": 7,
                "required": True,
            }
        ),
    )


    # ======================================================
    # HONEYPOT
    # ======================================================
    #
    # This field is intentionally hidden from normal users.
    # Basic automated bots often fill every available field.
    #
    # We reject the submission in clean() if this field
    # contains anything.
    # ======================================================

    website = forms.CharField(
        required=False,
        widget=forms.HiddenInput(),
    )


    # ======================================================
    # INITIALIZATION
    # ======================================================

    def __init__(self, *args, **kwargs):

        super().__init__(
            *args,
            **kwargs,
        )

        self.fields[
            "service"
        ].queryset = (
            Service.objects
            .filter(
                is_active=True,
            )
            .order_by(
                "number",
            )
        )


    # ======================================================
    # FULL NAME VALIDATION
    # ======================================================

    def clean_full_name(self):

        full_name = (
            self.cleaned_data[
                "full_name"
            ].strip()
        )

        if not full_name:

            raise forms.ValidationError(
                "Please enter your full name."
            )

        if len(full_name) < 2:

            raise forms.ValidationError(
                "Please enter a valid name."
            )

        return full_name


    # ======================================================
    # COMPANY NAME VALIDATION
    # ======================================================

    def clean_company_name(self):

        company_name = (
            self.cleaned_data.get(
                "company_name",
                "",
            )
            .strip()
        )

        return company_name


    # ======================================================
    # EMAIL VALIDATION
    # ======================================================

    def clean_email(self):

        email = (
            self.cleaned_data[
                "email"
            ]
            .strip()
            .lower()
        )

        return email


    # ======================================================
    # PHONE VALIDATION
    # ======================================================

    def clean_phone(self):

        phone = (
            self.cleaned_data[
                "phone"
            ]
            .strip()
        )

        # Allow:
        #
        # +254 739 651 744
        # 0739 651 744
        # +254-739-651-744
        # (0739) 651 744
        #
        # but reject letters and other unexpected characters.

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

        # Prevent obviously invalid values.
        digits = re.sub(
            r"\D",
            "",
            phone,
        )

        if len(digits) < 7:

            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        if len(digits) > 15:

            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        # A plus sign should only appear at the beginning.
        if "+" in phone and not phone.startswith("+"):

            raise forms.ValidationError(
                "Please enter a valid phone number."
            )

        return phone


    # ======================================================
    # MESSAGE VALIDATION
    # ======================================================

    def clean_message(self):

        message = (
            self.cleaned_data[
                "message"
            ].strip()
        )

        if len(message) < 10:

            raise forms.ValidationError(
                "Please provide a little more detail "
                "about how we can help."
            )

        return message


    # ======================================================
    # SPAM / HONEYPOT VALIDATION
    # ======================================================

    def clean_website(self):

        website = (
            self.cleaned_data.get(
                "website",
                "",
            )
            .strip()
        )

        if website:

            raise forms.ValidationError(
                "Unable to submit this form."
            )

        return website