# Generated by Django 4.0.3 on 2022-06-14 16:21

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_circularbanner'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='circularbanner',
            options={'verbose_name_plural': 'Circular Banners'},
        ),
        migrations.AlterModelOptions(
            name='homebanner',
            options={'verbose_name_plural': 'Home Banners'},
        ),
    ]
