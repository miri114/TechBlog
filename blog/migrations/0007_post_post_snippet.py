# Generated by Django 4.1.7 on 2023-03-07 17:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0006_alter_post_body'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='post_snippet',
            field=models.CharField(default='no-snippet for you', max_length=300),
        ),
    ]