from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
import random


def name_view(request):
    if request.method == "GET":
        return HttpResponse('Привет, меня зовут Селедцов Роман, мне 25')


def bio_view(request):
    if request.method == "GET":
        return HttpResponse('Увлекаюсь программированием, историей, компиком 😏 и т.д')


def datetime_view(request):
    if request.method == "GET":
        date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        return HttpResponse(f'Местное время {date_time} ⌛')


def count_view(request):
    if request.method == "GET":
        random_num = random.randint(1, 50)
        return HttpResponse(f'Твое случайное число {random_num} 🔢')
