# Generated by Django 5.1.4 on 2024-12-30 23:09

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candle", "0004_blogpost_thumbnail_alter_blogpost_published_date"),
    ]

    operations = [
        migrations.AlterField(
            model_name="blogpost",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                help_text="Featured image for the blog post",
                null=True,
                upload_to="blog_thumbnails/",
            ),
        ),
    ]