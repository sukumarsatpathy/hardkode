# Generated by Django 4.0.6 on 2022-08-03 14:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0004_userprofile_designation'),
    ]

    operations = [
        migrations.AddField(
            model_name='userprofile',
            name='company_name',
            field=models.CharField(blank=True, max_length=50, verbose_name='Company Name'),
        ),
    ]
