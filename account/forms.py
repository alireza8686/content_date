from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth.forms import AuthenticationForm
from django.core.exceptions import ValidationError


class SignUpForm(UserCreationForm):

    class Meta:
        model = User
        fields = ("first_name", "last_name", "username", "email", "password1", "password2")

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)
        # del self.fields['password2']
        self.fields['password1'].help_text = None
        self.fields['username'].help_text = None
        
        
    def clean(self):
          cleaned_data=super().clean()
          if User.objects.filter(username=cleaned_data["username"]).exists():
            raise ValidationError("این نام کاربری قبلا استفاده شده است. لطفاً نام کاربری دیگری انتخاب کنید.")
          

    def clean_password2(self):
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        if password1 and password2 and password1 != password2:
            raise ValidationError("گذرواژه‌ها باید یکسان باشند.")
        return password2
    
    def clean(self):
        cleaned_data = super().clean()
        
        first_name = cleaned_data.get("first_name")
        last_name = cleaned_data.get("last_name")
        username = cleaned_data.get("username")
        password1 = cleaned_data.get("password1")
        password2 = cleaned_data.get("password2")
        email = cleaned_data.get("email")

        if not first_name:
            raise ValidationError("لطفا نام خود را وارد کنید.")
        
        if not last_name:
            raise ValidationError("لطفا نام خانوادگی خود را وارد کنید.")
        
        if not username:
            raise ValidationError("لطفا نام کاربری خود را وارد کنید.")
        
        if not password1:
            raise ValidationError("لطفا گذرواژه خود را وارد کنید.")
        
        if not password2:
            raise ValidationError("لطفا تکرار گذرواژه خود را وارد کنید.")
        
        if not email:
            raise ValidationError("لطفا ایمیل خود را وارد کنید.")

        return cleaned_data


    


class LoginForm(AuthenticationForm):
    username = forms.CharField(widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Username'}))
    password = forms.CharField(widget=forms.PasswordInput(attrs={'class': 'form-control', 'placeholder': 'Password'}))

