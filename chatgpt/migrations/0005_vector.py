# Generated by Django 5.0.6 on 2024-06-11 05:15

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("chatgpt", "0004_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Vector",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("content", models.TextField()),
                ("category", models.CharField(max_length=100)),
            ],
        ),
    ]
