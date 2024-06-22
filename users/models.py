from django.core.validators import MinValueValidator, MaxValueValidator
from django.db.models.signals import post_save
from django.contrib.auth.models import User
from django.dispatch import receiver
from django.db import models


class CustomUser(User):
    GENDER_CHOICES = (
        ('Male', 'Male'),
        ('Female', 'Female',)
    )
    # username = models.CharField(max_length=30, required=True)
    age = models.PositiveIntegerField(default=18, validators=[
        MaxValueValidator(90),
        MinValueValidator(5),
    ])
    gender = models.CharField(max_length=10, choices=GENDER_CHOICES)
    group = models.CharField(max_length=20, default='Нет возрастной группы')


@receiver(post_save, sender=CustomUser)
def age_group(sender, instance, created, **kwargs):
    print('Пользователь успешно создан')
    age = instance.age
    if age < 5:
        instance.group = 'Дети'
    elif age >= 5 and age <= 10:
        instance.group = 'Дети'
    elif age >= 11 and age <= 18:
        instance.group = 'Подростки'
    elif age >= 18 and age <= 50:
        instance.group = 'Взрослые'
    else:
        instance.group = 'Нет возрастной группы'
    instance.save()
