# Generated by Django 4.0.6 on 2022-08-22 09:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('homeApp', '0004_maillist'),
    ]

    operations = [
        migrations.AlterField(
            model_name='maillist',
            name='contact_mail',
            field=models.EmailField(max_length=100, unique=True),
        ),
    ]