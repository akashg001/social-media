# Generated by Django 4.0 on 2022-04-07 14:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0003_remove_user_post_feed_remove_user_post_time_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user_post',
            name='slug',
        ),
    ]