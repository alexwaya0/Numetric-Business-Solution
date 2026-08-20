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
                "placeholder": "Full name",
                "autocomplete": "name",
                "required": True,
                "class": (
                    "w-full rounded-md border border-black/15 "
                    "bg-white px-4 py-3 text-sm text-numetric-dark "
                    "placeholder:text-black/35 outline-none "
                    "transition "
                    "focus:border-numetric-green "
                    "focus:ring-0"
                ),
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
                "placeholder": "Company name (optional)",
                "autocomplete": "organization",
                "class": (
                    "w-full rounded-md border border-black/15 "
                    "bg-white px-4 py-3 text-sm text-numetric-dark "
                    "placeholder:text-black/35 outline-none "
                    "transition "
                    "focus:border-numetric-green "
                    "focus:ring-0"
                ),
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
                "placeholder": "Email address",
                "autocomplete": "email",
                "inputmode": "email",
                "required": True,
                "class": (
                    "w-full rounded-md border border-black/15 "
                    "bg-white px-4 py-3 text-sm text-numetric-dark "
                    "placeholder:text-black/35 outline-none "
                    "transition "
                    "focus:border-numetric-green "
                    "focus:ring-0"
                ),
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
                "placeholder": "Phone number",
                "autocomplete": "tel",
                "inputmode": "tel",
                "required": True,
                "class": (
                    "w-full rounded-md border border-black/15 "
                    "bg-white px-4 py-3 text-sm text-numetric-dark "
                    "placeholder:text-black/35 outline-none "
                    "transition "
                    "focus:border-numetric-green "
                    "focus:ring-0"
                ),
            }
        ),
    )


    # ======================================================
    # SERVICE
    # ======================================================

    service = forms.ModelChoiceField(
        queryset=Service.objects.none(),
        label="Service Required",
        required=True,
        empty_label="Select a service",
        widget=forms.Select(
            attrs={
                "required": True,
                "class": (
                    "w-full rounded-md border border-black/15 "
                    "bg-white px-4 py-3 text-sm text-numetric-dark "
                    "outline-none "
                    "transition "
                    "focus:border-numetric-green "
                    "focus:ring-0"
                ),
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
                "placeholder": (
                    "Tell us briefly how we can help..."
                ),
                "rows": 6,
                "required": True,
                "class": (
                    "w-full resize-y rounded-md "
                    "border border-black/15 bg-white "
                    "px-4 py-3 text-sm leading-6 "
                    "text-numetric-dark "
                    "placeholder:text-black/35 "
                    "outline-none transition "
                    "focus:border-numetric-green "
                    "focus:ring-0"
                ),
            }
        ),
    )


    # ======================================================
    # HONEYPOT
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

        self.fields["service"].queryset = (
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
            self.cleaned_data["full_name"]
            .strip()
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
            self.cleaned_data["email"]
            .strip()
            .lower()
        )

        return email


    # ======================================================
    # PHONE VALIDATION
    # ======================================================

    def clean_phone(self):

        phone = (
            self.cleaned_data["phone"]
            .strip()
        )

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
            self.cleaned_data["message"]
            .strip()
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