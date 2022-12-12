# Generated by Django 4.1.3 on 2022-11-13 06:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ion", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="comment",
            name="image",
            field=models.ImageField(blank=True, upload_to="comment_images/"),
        ),
        migrations.AddField(
            model_name="post",
            name="image",
            field=models.ImageField(blank=True, upload_to="post_images/"),
        ),
    ]
