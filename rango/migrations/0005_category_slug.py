# Generated by Django 5.1.5 on 2025-02-13 14:30

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0004_remove_page_likes_category_likes_category_views"),
    ]

    operations = [
        migrations.AddField(
            model_name="category",
            name="slug",
            field=models.SlugField(default=""),
            preserve_default=False,
        ),
    ]
