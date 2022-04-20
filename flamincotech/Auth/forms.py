from django import forms

from Admin1.models import NewUser
class AddMember(forms.ModelForm):
    class Meta:
        model=NewUser
        fields=['email','user_name','first_name','Address','password']
        widgets = {
        'password': forms.PasswordInput()
        }
class LoginMember(forms.ModelForm):
    class Meta:
        model=NewUser
        fields=['email','password']
        widgets = {
        'password': forms.PasswordInput()
        }
