# Generated by Django 5.1.5 on 2025-02-06 16:05

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("rango", "0002_alter_category_options"),
    ]

    operations = [
        migrations.AddField(
            model_name="page",
            name="likes",
            field=models.IntegerField(default=0),
        ),
    ]
