from django.contrib.auth.forms import UserCreationForm
from django.db import models
from django.contrib.auth.models import User
from django import forms
from django.db.models.signals import post_save
from django.dispatch import receiver
from . import models

GENDER_CHOICES = (
    ('M', 'Male'),
    ('F', 'Female',)
)


class CustomRegistrationForm(UserCreationForm):
    username = forms.CharField(max_length=30, required=True)
    first_name = forms.CharField(max_length=30, required=True)
    last_name = forms.CharField(max_length=30, required=True)
    hobby = forms.CharField(max_length=300, required=True)
    gender = forms.ChoiceField(choices=GENDER_CHOICES, required=True)
    email = forms.EmailField(max_length=254, required=False)
    address = forms.CharField(max_length=255, required=False)
    city = forms.CharField(max_length=100, required=False)
    country = forms.CharField(max_length=100, required=True)
    age = forms.IntegerField(required=True)

    class Meta:
        model = User
        fields = (
            'username',
            'email',
            'gender',
            'password1',
            'password2',
            'first_name',
            'last_name',
            'age',
            'country',
            'city',
            'hobby',

        )

    def save(self, commit=True):
        user = super(CustomRegistrationForm, self).save(commit=False)
        user.email = self.cleaned_data['email']
        if commit:
            user.save()
        return user


@receiver(post_save, sender=models.CustomUser)
def age_group(sender, instance, created, **kwargs):
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
