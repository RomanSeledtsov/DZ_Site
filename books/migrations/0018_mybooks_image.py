# Generated by Django 5.0.6 on 2024-06-13 12:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_alter_books_options_alter_mybooks_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='mybooks',
            name='image',
            field=models.ImageField(default='path/to/default/image.jpg', upload_to=''),
        ),
    ]