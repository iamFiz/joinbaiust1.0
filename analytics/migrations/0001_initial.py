# Generated by Django 4.0.3 on 2022-06-21 16:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('application', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ApplicationNewsSource',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('information_source', models.CharField(max_length=100)),
                ('information_source_details', models.CharField(blank=True, max_length=100, null=True)),
                ('application_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='newssource', to='application.applicantextrainformation')),
            ],
            options={
                'verbose_name_plural': 'Application News Sources',
            },
        ),
        migrations.CreateModel(
            name='ApplicantWorkingExperience',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('has_working_experience', models.BooleanField(default=False)),
                ('working_experience_details', models.TextField(blank=True, null=True)),
                ('application_info', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='workexperience', to='application.applicantextrainformation')),
            ],
            options={
                'verbose_name_plural': 'Applicant Working Experiences',
            },
        ),
    ]
