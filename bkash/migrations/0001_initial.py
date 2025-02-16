# Generated by Django 4.2.1 on 2023-05-12 15:47

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PaymentReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('payer_reference', models.CharField(max_length=50)),
                ('merchant_invoice_number', models.CharField(max_length=50)),
            ],
            options={
                'verbose_name': 'Payment Reference',
                'verbose_name_plural': 'Payment References',
                'ordering': ['-created_at'],
            },
        ),
    ]
