# Generated by Django 4.1.7 on 2023-03-13 12:08

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_userprofile_facebook_url_userprofile_instagram_url_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='pinterest_url',
            new_name='github_url',
        ),
    ]