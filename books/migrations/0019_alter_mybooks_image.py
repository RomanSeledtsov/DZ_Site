# Generated by Django 5.0.6 on 2024-06-13 12:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0018_mybooks_image"),
    ]

    operations = [
        migrations.AlterField(
            model_name="mybooks",
            name="image",
            field=models.ImageField(default="images/", upload_to=""),
        ),
    ]
