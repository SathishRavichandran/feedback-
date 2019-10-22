from django.shortcuts import render, redirect
from django.http import HttpResponse,request
from django.utils.crypto import get_random_string

from users.models import UsersProfile
from users.forms import UserForm
from django.contrib.auth.models import User
from django.core.mail import send_mail

import pdb

# Create your views here.

def load_sidebar(request):
    if request.method == 'POST':
        try:
            # Try to find a user matching your username
            user = User.objects.get(username=request._post['username'])

            #  Check the password is the reverse of the username
            if user:
                return render(request, "sidebar_template.html")
            else:
                # No? return None - triggers default login failed
                return None
        except User.DoesNotExist:
            # No user was found, return None - triggers default login failed
            return None

        pass
    else:
        return render(request, "custom_login.html")


def create_user(request):
    if request.method== "POST":
        form = UserForm(request.POST)
        if form.is_valid():
            password = get_random_string(length=7)
            data = {
                'user_name': form.data['user_name'],
                'email' : form.data['email'],
                'password': password
            }
            auth = User.objects.create_user(data)
            user_profile = UsersProfile()
            user_profile.email = form.data['email']
            user_profile.user_type = form.data['user_type']
            user_profile.user_name = form.data['user_name']
            user_profile.user = auth
            user_profile.save()
            # send_mail(
            #     'Customer creation',
            #     'Please find the credentials.',
            #     'from_email',
            #     [form.data['email']],
            #     html_message= 'username :% s' % form.data['user_name'],
            #     fail_silently=False,
            # )
            return redirect('/customer_list')

    else:
        form = UserForm()
    return render(request, 'create_user.html', {'form': form})


def show(request):
    employees = UsersProfile.objects.all()
    return render(request, "user_list.html", {'employees': employees})