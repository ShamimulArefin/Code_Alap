from django.shortcuts import render
from homeApp import forms
from homeApp.models import Contact

from django.http import *
from django.urls import reverse

# Create your views here.

def home(request):
    dict = {'title':'Code Alap', 'meta_title':'Code Alap', 'meta_description':'Code Alap, an informative and learning platform. Programming or coding resources and solutions with guidelines. Great for Technology updates.', }
    return render(request, 'homeApp/home.html', context=dict)

def notFound(request, exception):
    dict = {'title':'404'}
    return render(request, 'homeApp/404.html', context=dict)

def subscription(request):
    if request.method == 'POST':
        subs = forms.MailListForm(request.POST)
        if subs.is_valid():
            subs.save(commit=True)
    return render(request, 'base.html', context={})

def contact(request):
    dict = {'title':'Contact with Code Alap'}
    if request.method == 'POST':
        form = forms.ContactForm(request.POST)
        mailForm = forms.MailListForm(request.POST)
        if form.is_valid():
            form.save(commit=True)
            dict.update({'success_text':'Message sent successfully!'})
        if mailForm.is_valid():
            mailForm.save(commit=True)
    return render(request, 'homeApp/contact.html', context=dict)

def viewMessages(request):
    dict = {'title':'All Messages From Contact Form'}
    messageList = Contact.objects.all().order_by('-pk')
    dict.update({'messageList': messageList})
    return render(request, 'homeApp/view_contacts.html', context=dict)

def deleteMessage(request, message_id):
    message = Contact.objects.get(pk=message_id).delete()
    return HttpResponseRedirect(reverse('homeApp:viewMessages'))
