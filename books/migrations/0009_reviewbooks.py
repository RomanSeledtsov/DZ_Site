# Generated by Django 5.0.6 on 2024-06-09 13:00

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0008_alter_books_genre"),
    ]

    operations = [
        migrations.CreateModel(
            name="ReviewBooks",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("text", models.TextField()),
                ("stars", models.IntegerField()),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                (
                    "reviews_book",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="reviews_books",
                        to="books.books",
                    ),
                ),
            ],
        ),
    ]
