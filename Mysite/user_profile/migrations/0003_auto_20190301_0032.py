# Generated by Django 2.1.7 on 2019-02-28 18:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0002_auto_20190228_2253'),
    ]

    operations = [
        migrations.AddField(
            model_name='profile',
            name='avatar_path',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='profile',
            name='avatar_url',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]