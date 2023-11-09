from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=100)
    contact_mail = models.EmailField(max_length=100)
    subject = models.CharField(max_length=200)
    message = models.TextField(max_length=2000)

    def __str__(self):
        return self.subject

class MailList(models.Model):
    name = models.CharField(max_length=100)
    contact_mail = models.EmailField(max_length=100, unique=True)

    def __str__(self):
        return self.name