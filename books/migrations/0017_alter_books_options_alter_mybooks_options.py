# Generated by Django 5.0.6 on 2024-06-09 15:26

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0016_alter_mybooks_options_mybooks_tags'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='books',
            options={'verbose_name': 'Книгу', 'verbose_name_plural': 'Все книги'},
        ),
        migrations.AlterModelOptions(
            name='mybooks',
            options={'verbose_name': 'вашу книгу', 'verbose_name_plural': 'Книги с тегами'},
        ),
    ]