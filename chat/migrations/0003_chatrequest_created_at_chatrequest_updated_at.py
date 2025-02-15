# Generated by Django 4.0.3 on 2022-04-15 21:16

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('chat', '0002_alter_chatrequest_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='chatrequest',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='chatrequest',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
