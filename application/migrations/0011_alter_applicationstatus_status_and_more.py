# Generated by Django 4.1.7 on 2023-05-03 23:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0010_alter_applicantextrainformation_permanent_address'),
    ]

    operations = [
        migrations.AlterField(
            model_name='applicationstatus',
            name='status',
            field=models.CharField(choices=[('application_submitted', 'Application Submitted'), ('awaiting_payment', 'Awaiting Payment'), ('awaiting_payment_reminder', 'Awaiting Payment Reminder'), ('payment_not_received', 'Payment Not Received in T'), ('under_review', 'Under Review'), ('payment_completed', 'Payment Completed'), ('photo_submitted', 'Photo and Signature Uploaded'), ('download_admit', 'Download Admit'), ('payment_verified', 'Payment Verified-FORSMS'), ('payment_not_verified', 'Payment Not Verified-FORSMS'), ('application_cancelled', 'Application Cancelled'), ('remind_upload_photo', 'Remind To Upload Photo'), ('notify_venue_as_sylhet', 'Notify Venue as Sylhet'), ('notify_venue_as_dhaka', 'Notify Venue as Dhaka'), ('notify_dummy_venue_location', 'Notify  Dummy Venue Location')], default='application_submitted', max_length=100),
        ),
        migrations.AlterField(
            model_name='applicationstatuschangelog',
            name='new_status',
            field=models.CharField(choices=[('application_submitted', 'Application Submitted'), ('awaiting_payment', 'Awaiting Payment'), ('awaiting_payment_reminder', 'Awaiting Payment Reminder'), ('payment_not_received', 'Payment Not Received in T'), ('under_review', 'Under Review'), ('payment_completed', 'Payment Completed'), ('photo_submitted', 'Photo and Signature Uploaded'), ('download_admit', 'Download Admit'), ('payment_verified', 'Payment Verified-FORSMS'), ('payment_not_verified', 'Payment Not Verified-FORSMS'), ('application_cancelled', 'Application Cancelled'), ('remind_upload_photo', 'Remind To Upload Photo'), ('notify_venue_as_sylhet', 'Notify Venue as Sylhet'), ('notify_venue_as_dhaka', 'Notify Venue as Dhaka'), ('notify_dummy_venue_location', 'Notify  Dummy Venue Location')], max_length=100),
        ),
        migrations.AlterField(
            model_name='applicationstatuschangelog',
            name='previous_status',
            field=models.CharField(choices=[('application_submitted', 'Application Submitted'), ('awaiting_payment', 'Awaiting Payment'), ('awaiting_payment_reminder', 'Awaiting Payment Reminder'), ('payment_not_received', 'Payment Not Received in T'), ('under_review', 'Under Review'), ('payment_completed', 'Payment Completed'), ('photo_submitted', 'Photo and Signature Uploaded'), ('download_admit', 'Download Admit'), ('payment_verified', 'Payment Verified-FORSMS'), ('payment_not_verified', 'Payment Not Verified-FORSMS'), ('application_cancelled', 'Application Cancelled'), ('remind_upload_photo', 'Remind To Upload Photo'), ('notify_venue_as_sylhet', 'Notify Venue as Sylhet'), ('notify_venue_as_dhaka', 'Notify Venue as Dhaka'), ('notify_dummy_venue_location', 'Notify  Dummy Venue Location')], max_length=100),
        ),
    ]
