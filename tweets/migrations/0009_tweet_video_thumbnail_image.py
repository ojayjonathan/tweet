# Generated by Django 3.0.3 on 2020-03-20 11:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tweets', '0008_auto_20200320_1131'),
    ]

    operations = [
        migrations.AddField(
            model_name='tweet',
            name='video_thumbnail_image',
            field=models.ImageField(null=True, upload_to='video/thumbnails'),
        ),
    ]