# Generated by Django 3.1.2 on 2020-10-07 16:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0003_auto_20201007_0810'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='description',
            field=models.TextField(blank=True, null=True, verbose_name='О профиле'),
        ),
        migrations.AddField(
            model_name='profile',
            name='profile_photo',
            field=models.ImageField(default='/media/default_pic.jpg/', upload_to='profiles'),
        ),
    ]
