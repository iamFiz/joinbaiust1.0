# Generated by Django 4.1.7 on 2023-02-21 15:18

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('newsletter', '0007_alter_statusemail_status_alter_statussms_status'),
    ]

    operations = [
        migrations.AddField(
            model_name='emailcontent',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='emailcontent',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='batch',
            field=models.CharField(choices=[('BBA10', 'BBA10'), ('BBA11', 'BBA11')], default='BBA11', max_length=25),
        ),
        migrations.AddField(
            model_name='newsletter',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='newsletter',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='statusemail',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statusemail',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='statusemailfiles',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statusemailfiles',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='statussms',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='statussms',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='batch',
            field=models.CharField(choices=[('BBA10', 'BBA10'), ('BBA11', 'BBA11')], default='BBA11', max_length=25),
        ),
        migrations.AddField(
            model_name='subscriber',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='subscriber',
            name='updated_at',
            field=models.DateTimeField(auto_now=True),
        ),
    ]
