# Generated by Django 5.0.6 on 2024-06-09 13:31

import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0011_alter_reviewbooks_options'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviewbooks',
            name='stars',
            field=models.PositiveIntegerField(validators=[django.core.validators.MinValueValidator(1), django.core.validators.MaxValueValidator(10)]),
        ),
    ]