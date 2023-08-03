from project.celery import app
from .models import Profile
import os
import datetime
from django.core.mail import send_mail


@app.task(name="send_me_mail")
def send_me_mail():
    try:
        time_thresold = datetime.datetime.now() - datetime.timedelta(minutes=2)
        profiles = Profile.objects.filter(is_verified=False)
        
        for profile in profiles:
            subject = 'Please verify your account'
            message = 'your account is not verified.'
            email_from = os.getenv('EMAIL_HOST_USER')
            recipient_list = [profile.email]
            send_mail(subject,message,email_from,recipient_list)
            print("okoghdfgdfgfdg")
    except Exception as e:
        print(e)
