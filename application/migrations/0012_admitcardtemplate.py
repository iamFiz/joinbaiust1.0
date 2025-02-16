# Generated by Django 4.2.1 on 2023-05-23 20:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('application', '0011_alter_applicationstatus_status_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdmitCardTemplate',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('name', models.CharField(max_length=255)),
                ('template', models.FileField(upload_to='application/admit_card_templates/')),
                ('venue', models.CharField(choices=[('Mirpur Cantonment', 'Mirpur Cantonment')], max_length=255)),
            ],
            options={
                'abstract': False,
            },
        ),
    ]
