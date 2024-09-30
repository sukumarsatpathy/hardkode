# Generated by Django 4.0.6 on 2022-08-03 11:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_alter_userprofile_user_type'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_1',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='address_line_2',
        ),
        migrations.AddField(
            model_name='userprofile',
            name='fb_url',
            field=models.URLField(blank=True, max_length=100, verbose_name='Facebook'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='gh_url',
            field=models.URLField(blank=True, max_length=100, verbose_name='GitHub'),
        ),
        migrations.AddField(
            model_name='userprofile',
            name='tw_url',
            field=models.URLField(blank=True, max_length=100, verbose_name='Twitter'),
        ),
    ]
