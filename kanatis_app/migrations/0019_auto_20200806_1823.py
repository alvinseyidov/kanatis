# Generated by Django 3.0.8 on 2020-08-06 18:23

import ckeditor.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('kanatis_app', '0018_auto_20200806_1731'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='service',
            name='fa_class',
        ),
        migrations.CreateModel(
            name='SubAboutUs',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=255, null=True)),
                ('img', models.ImageField(upload_to='subabout/')),
                ('description', ckeditor.fields.RichTextField()),
                ('slug', models.SlugField(editable=False, null=True, unique=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('about', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subabouts', to='kanatis_app.AboutUs')),
            ],
            options={
                'verbose_name_plural': 'Haqqımızda',
            },
        ),
    ]
