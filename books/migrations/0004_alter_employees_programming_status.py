# Generated by Django 5.0.6 on 2024-06-06 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0003_remove_employees_age'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employees',
            name='programming_status',
            field=models.CharField(choices=[('Full Stack', 'Full Stack'), ('Frontend Development', 'Frontend Development'), ('Backend Development', 'Backend Development'), ('Javascript Development', 'Javascript Development')], max_length=100, null=True),
        ),
    ]