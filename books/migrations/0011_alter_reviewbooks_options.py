# Generated by Django 5.0.6 on 2024-06-09 13:06

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0010_alter_reviewbooks_stars'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='reviewbooks',
            options={'verbose_name': 'Отзыв', 'verbose_name_plural': 'Отзывы'},
        ),
    ]