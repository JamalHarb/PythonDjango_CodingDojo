from email import message
from django.db import models
from login_registration_app.models import User
from datetime import datetime
from dateutil.relativedelta import relativedelta


# Create your models here.
class Message(models.Model):
    message = models.TextField()
    user = models.ForeignKey(User, related_name='messages', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    comment = models.TextField()
    user = models.ForeignKey(User, related_name='comments', on_delete=models.CASCADE)
    message = models.ForeignKey(Message, related_name='comments', on_delete=models.CASCADE, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

def create_message(request):
    some_message = Message.objects.create(
        message = request.POST['message'],
        user = User.objects.get(email=request.session['email'])
    )

def create_comment(request):
    msg_id = int(request.POST['which-message'])
    some_comment = Comment.objects.create(
        comment = request.POST['comment'],
        user = User.objects.get(email=request.session['email']),
        message = Message.objects.get(id=msg_id)
    )

def all_messages():
    return reversed(Message.objects.all())

def all_comments():
    return Comment.objects.all()

def delete_message(request):
    msg_id = int(request.POST['message-to-delete'])
    msg = Message.objects.get(id=msg_id)
    if msg.created_at > datetime.now() - relativedelta(minutes=30):
        msg.delete()

def time_before_30mins():
    return datetime.now() - relativedelta(minutes=30)