from django import forms
from django.contrib.auth import get_user_model, authenticate 
from django.core.exceptions import ValidationError

User = get_user_model()

class UserRegisterForm(forms.ModelForm):
    password1 = forms.CharField(
        label="Password",
        min_length=8,
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
    )
    password2 = forms.CharField(
        label="Confirm password",
        widget=forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Confirm password"}),
    )

    class Meta:
        model = User
        fields = (
            "username",
            "email",
            "gender",
            "birth_date",
            "country",
        )
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Jane Doe"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "jane@example.com"}),
            "gender": forms.Select(attrs={"class": "form-control"}),
            "country": forms.Select(attrs={"class": "form-control"}),
            "birth_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }
    def clean_email(self):
        email = self.cleaned_data.get("email")
        if User.objects.filter(email=email).exists():
            raise ValidationError("A user with this email already exists.")
        return email

    def clean(self):
        cleaned_data = super().clean()
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")

        if password1 and password2 and password1 != password2:
            self.add_error('password2', "Passwords don't match.")
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.set_password(self.cleaned_data["password1"])
        if commit:
            user.save()
        return user


class UserLoginForm(forms.Form):
    username = forms.CharField(
        widget=forms.TextInput(attrs={
            'class': 'form-control',
            'placeholder': 'Username'}),
        label='Username'
    )
    password = forms.CharField(
        widget=forms.PasswordInput(attrs={
            'class': 'form-control',
            "placeholder": 'Password'}),
        label='password'
    )

    def clean(self):
        cleaned_data = super().clean()
        username = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username and password:
            user = authenticate(username=username, password=password)
            if not user:
                raise ValidationError('Invalid username or password')
            cleaned_data['user'] = user
        return cleaned_data



