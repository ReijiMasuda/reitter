# Generated by Django 4.2.6 on 2024-03-30 05:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('a', '0003_delete_post_tweet_created_at'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='tweet',
            name='point',
        ),
        migrations.AlterField(
            model_name='tweet',
            name='name',
            field=models.CharField(max_length=10),
        ),
    ]
