# Generated by Django 3.0.3 on 2020-03-14 19:18

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0003_remove_tweet_country'),
    ]

    operations = [
        migrations.AlterField(
            model_name='tweet',
            name='created_date',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
