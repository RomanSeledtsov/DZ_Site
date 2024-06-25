# Generated by Django 5.0.6 on 2024-06-06 10:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("books", "0006_rename_employees_books"),
    ]

    operations = [
        migrations.AlterModelOptions(
            name="books",
            options={"verbose_name": "Книгу", "verbose_name_plural": "Книги"},
        ),
        migrations.RenameField(
            model_name="books",
            old_name="about_emp",
            new_name="about_book",
        ),
        migrations.RemoveField(
            model_name="books",
            name="birthday",
        ),
        migrations.RemoveField(
            model_name="books",
            name="github",
        ),
        migrations.RemoveField(
            model_name="books",
            name="programming_status",
        ),
        migrations.RemoveField(
            model_name="books",
            name="rezume",
        ),
        migrations.AddField(
            model_name="books",
            name="genre",
            field=models.CharField(
                choices=[
                    ("Romance", "Romance"),
                    ("Fiction", "Fiction"),
                    ("Fantasy", "Fantasy"),
                    ("Science fiction", "Science fiction"),
                ],
                max_length=20,
                null=True,
            ),
        ),
    ]
