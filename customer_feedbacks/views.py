# Create your views here.
from django.shortcuts import render, redirect
from django.http import HttpResponse,request
from django.views import View
from django.views.generic import ListView
from django.shortcuts import get_object_or_404

from customer_feedbacks.models import Feedbacks


class CustomerFeedback(object):

    def get_customer_feedbacks(request, *args, **kwargs):
        queryset = Feedbacks.objects.all()
        records = []
        for record in list(queryset):
            items = {
                'feedback_ratings' : range(0, int(record.ratings)),
                'pending_ratings' : range(0, (5- int(record.ratings))),
                'text' : record.feedback_text
            }
            records.append(items)

        return render(request, 'feedback_ratings.html',
                      {'feedback':records,
                       })

    def create_feedback(request):
        if request.method == 'POST':
            try:
                feed_obj = Feedbacks()
                feed_obj.feedback_text = request.POST['feedback']
                feed_obj.ratings = request.POST['ratings']
                feed_obj.user = request.user.profile
                feed_obj.save()
            except:
                pass
        return render(request, 'add_feedback_form.html')
