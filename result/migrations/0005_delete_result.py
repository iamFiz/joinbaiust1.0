# Generated by Django 4.0.3 on 2022-06-29 15:41

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('result', '0004_remove_result_passed_result_remarks'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Result',
        ),
    ]
