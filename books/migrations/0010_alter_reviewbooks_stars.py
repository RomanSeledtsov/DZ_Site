# Generated by Django 5.0.6 on 2024-06-09 13:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0009_reviewbooks'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewbooks',
            name='stars',
            field=models.PositiveIntegerField(),
        ),
    ]
