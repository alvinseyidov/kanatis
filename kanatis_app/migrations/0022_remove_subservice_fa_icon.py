# Generated by Django 3.0.8 on 2020-08-28 09:10

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0021_auto_20200806_2005'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='subservice',
            name='fa_icon',
        ),
    ]
