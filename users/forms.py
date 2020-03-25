from django import forms
from django.contrib.auth.forms import UserCreationForm, UserChangeForm

from .models import CustomUser


class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        #fields = UserCreationForm.Meta.fields + ('age',) #Esto es usando por defecto el login de django
        fields = ( 'username','first_name', 'last_name','email','photo',) #Estos campos pedirá para hacer un Sign Up


class CustomUserChangeForm(UserChangeForm):

    class Meta:
        model = CustomUser
        #fields = UserChangeForm.Meta.fields #Esto es usando por defecto el login de django
        fields = ( 'username','first_name', 'last_name','email','photo',) #Estos campos pedirá para hacer cambios

        
