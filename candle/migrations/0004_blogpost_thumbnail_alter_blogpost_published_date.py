# Generated by Django 5.1.4 on 2024-12-30 23:08

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("candle", "0003_config_pinterest_url"),
    ]

    operations = [
        migrations.AddField(
            model_name="blogpost",
            name="thumbnail",
            field=models.ImageField(
                blank=True,
                help_text="Featured image for the blog post",
                null=True,
                upload_to="blog_images/",
            ),
        ),
        migrations.AlterField(
            model_name="blogpost",
            name="published_date",
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
