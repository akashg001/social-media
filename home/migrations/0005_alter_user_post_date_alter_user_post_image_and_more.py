# Generated by Django 4.0.3 on 2022-04-09 11:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0004_remove_user_post_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user_post',
            name='date',
            field=models.DateTimeField(auto_now_add=True),
        ),
        migrations.AlterField(
            model_name='user_post',
            name='image',
            field=models.ImageField(upload_to='home/image'),
        ),
        migrations.AlterField(
            model_name='user_post',
            name='likes',
            field=models.BigIntegerField(null=True),
        ),
    ]
