# Generated by Django 4.0.3 on 2022-04-20 19:16

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0004_chatrequest_area'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='chatrequest',
            options={'verbose_name_plural': 'Chat Requests'},
        ),
    ]
