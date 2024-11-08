from django import forms
from django.contrib.auth.models import User
from .models import Profile


class LoginForm(forms.Form):
    """
    LoginForm is a Django form for user authentication.

    Fields:
        username (CharField): A text field for the username with a maximum length of 100 characters.
        password (CharField): A password field for the password with a maximum length of 100 characters.

    Both fields use Bootstrap's 'form-control' class for styling.
    """
    username = forms.CharField(
        label="Username",
        widget=forms.TextInput(attrs={"class": "form-control"}),
        max_length=100,
    )
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
        max_length=100,
    )


class UserRegistrationForm(forms.ModelForm):
    """
    UserRegistrationForm is a Django ModelForm for user registration.

    Fields:
        password (CharField): A password input field with a form-control CSS class.
        password2 (CharField): A repeat password input field with a form-control CSS class.
        date_of_birth (DateField): A date input field for the user's date of birth with a form-control CSS class.
        health_card (CharField): A text input field for the user's health card with a form-control CSS class.

    Meta:
        model (User): The model associated with this form.
        fields (tuple): The fields to include in the form, specifically 'username' and 'email'.

    Methods:
        clean_password2(): Validates that the password and repeat password fields match. Raises a ValidationError if they do not.
    """
    password = forms.CharField(
        label="Password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )
    password2 = forms.CharField(
        label="Repeat password",
        widget=forms.PasswordInput(attrs={"class": "form-control"}),
    )

    date_of_birth = forms.DateField(
        label="Date of Birth",
        widget=forms.DateInput(attrs={"class": "form-control"}),
    )

    health_card = forms.CharField(
        label="Health Card",
        widget=forms.TextInput(attrs={"class": "form-control"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
        )

    def clean_password2(self):
        cd = self.cleaned_data
        if cd["password"] != cd["password2"]:
            raise forms.ValidationError("Passwords don't match.")
        return cd["password2"]


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ("first_name", "last_name", "email")
