from django import forms

from Admin1.models import NewUser
class AddMember(forms.ModelForm):
    confirm_password=forms.CharField(widget=forms.PasswordInput())
    class Meta:
        model=NewUser
        fields=['email','user_name','first_name','password','is_superuser']
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
