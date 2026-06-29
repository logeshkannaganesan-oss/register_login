import re
from django import forms
from .models import UserRegister

class RegisterForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput(), label="Confirm Password")

    class Meta:
        model = UserRegister
        fields = ['username', 'email', 'mobile', 'password']
        widgets = {
            'password': forms.PasswordInput(),
        }

    def clean_mobile(self):
        mobile = self.cleaned_data.get('mobile')
        if not re.match(r'^[6-9]\d{9}$', mobile):
            raise forms.ValidationError("Enter a valid 10-digit Indian mobile number starting with 6-9.")
        return mobile

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password and confirm_password and password != confirm_password:
            raise forms.ValidationError("Passwords do not match!")
        return cleaned_data