"""feedback URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from users import views
from django.conf.urls import include, url
from customer_feedbacks.views import CustomerFeedback
from django.http import HttpRequest


urlpatterns = [
    path('', views.load_sidebar),
    url(r'app', views.load_sidebar),
    url(r'users', views.create_user),
    url(r'customer_list', views.show),
    url(r'feedback_ratings',CustomerFeedback.get_customer_feedbacks),
    url(r'add_feedback', CustomerFeedback.create_feedback)

]
