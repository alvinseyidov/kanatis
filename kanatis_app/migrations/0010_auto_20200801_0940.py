# Generated by Django 3.0.8 on 2020-08-01 09:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0009_auto_20200801_0937'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='gmap_embed_address',
            field=models.CharField(max_length=1000, verbose_name='Gmap embeded iframe'),
        ),
    ]