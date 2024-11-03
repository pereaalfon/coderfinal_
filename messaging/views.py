# messaging/views.py
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Message
from django.contrib.auth.models import User

@login_required
def send_message(request, receiver_id):
    receiver = User.objects.get(id=receiver_id)
    if request.method == 'POST':
        content = request.POST['content']
        message = Message(sender=request.user, receiver=receiver, content=content)
        message.save()
        return redirect('inbox')
    return render(request, 'messaging/send_message.html', {'receiver': receiver})

@login_required
def inbox(request):
    received_messages = Message.objects.filter(receiver=request.user).order_by('-timestamp')
    return render(request, 'messaging/inbox.html', {'received_messages': received_messages})
