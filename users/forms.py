from django import forms
from users.models import UsersProfile

class UserForm(forms.Form):
    class Meta:
        model = UsersProfile
        fields = ('email','user_type',)
