
from django import forms
from django.core import validators

from .models import User


def validate_email(value):
    if 'gmail.com' not in value:
        print("Raise Error")
        raise forms.ValidationError("Gmail accepted only")
    
def validate_name_length(value):
    if len(value) < 5:
        print("Raise Error")
        raise forms.ValidationError("Name must be 5 characters or longer")
    
def validate_name_letter(value):
    if value[0].lower() != 'z':
        print("Raise Error - First Letter Not Z")
        raise forms.ValidationError("Name must begin with the letter Z")


class FormName(forms.Form):
    name = forms.CharField(validators=[validators.MinLengthValidator(5),validate_name_letter])
    email = forms.EmailField(validators=[validators.MinLengthValidator(15),validate_email])
    v_email = forms.EmailField()
    text = forms.CharField(widget=forms.Textarea)
    
    def clean(self):

        if self.is_valid():
           data = super().clean()
           email = data['email']
           v_email = data['v_email']
           print("Clean Method 2")

           if v_email != email:
              print("Raise Error - Emails Different")
              raise forms.ValidationError("The emails are not the same")
           
class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'