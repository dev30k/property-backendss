from.models import MyUser
from django import forms
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.contrib.auth.forms import UserChangeForm, UserCreationForm


class MyUserCreationForm(UserCreationForm):
    first_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
        'class':'form-control',
        'placeholder':'first name',
        }))
    last_name = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'surname',
    }))
    nat_id = forms.CharField(
        required=True,
        widget=forms.TextInput(attrs={
        'class':'form-control',
         'placeholder':'national id',
    }))
    email = forms.EmailField(
        required=True,
        widget=forms.EmailInput(attrs={
        'class':'form-control',
         'placeholder':'someone@mail.com',
    }))
    phone_number = forms.IntegerField(
        required=True,
        widget=forms.NumberInput(attrs={
        'placeholder':'254712345678',
        'class':'form-control'
    }))
    password1 = forms.CharField(
        label='Password',
        max_length = 32,
        required=True,
        widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))

    password2 = forms.CharField(
        label='Confirm',
        max_length = 32,
        required=True,
        widget=forms.PasswordInput(attrs={
        'class':'form-control'
    }))

    class Meta:
        model = MyUser
        fields = ['first_name','last_name','nat_id', 'email','phone_number', 'password1', 'password2',]


        def clean_national_id(self):
            nat_id = self.cleaned_data['nat_id']
            try:
                MyUser.objects.get(nat_id=nat_id)
            except MyUser.DoesNotExist:
                return nat_id
            raise ValidationError(self.error_messages['duplicate_national_id'])
        
        def clean_email(self):
            email = self.cleaned_data.get("email")
            qs = MyUser.objects.get(email=email)
            if qs.exists():
                raise forms.ValidationError("This email is already in use")
            
            return email

        def clean_password2(self):
            # Check that the two password entries match
            password1 = self.cleaned_data.get("password1")
            password2 = self.cleaned_data.get("password2")
            if password1 and password2 and password1 != password2:
                raise forms.ValidationError("Passwords don't match")
            return password2

        def save(self, commit=True):
            user = super(UserCreationForm, self).save(commit=False)
            user.set_password(self.cleaned_data["password1"])
            if commit:
                user.save()
            return user

class MyUserChangeForm(UserChangeForm):
    password = ReadOnlyPasswordHashField()
    
    class Meta:
        model = MyUser
        fields = ('nat_id', 'password', 'email',
            'first_name','last_name', 'phone_number','password')


class LoginForm(forms.Form):
    email = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder" : "email",                
                "class": "form-control"
            }
        ))
    password = forms.CharField(
        widget=forms.PasswordInput(
            attrs={
                "placeholder" : "Password",                
                "class": "form-control"
            }
        ))