# Generated by Django 5.0.6 on 2024-06-20 08:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0022_quote"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="quote",
            options={"verbose_name": "Цитату", "verbose_name_plural": "Цитаты"},
        ),
    ]
