from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from .models import User
from captcha.fields import ReCaptchaField
from captcha.widgets import ReCaptchaV3

class my_user_creation_form(UserCreationForm):
    
    captcha = ReCaptchaField(widget=ReCaptchaV3)

    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']

class update_user_form(ModelForm):
    class Meta:
        model = User
        fields = ['email', 'phone_number', 'bio', 'avatar']