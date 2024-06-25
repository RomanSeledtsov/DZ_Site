from django.shortcuts import render
from django.http import HttpResponse


def hello_view(request):
    if request.method == "GET":
        return HttpResponse("Привет мир")


def news_view(request):
    if request.method == "GET":
        return HttpResponse(
            "Правление Национального банка Кыргызстана 27 мая 2024 года приняло решение снизить учетную ставку (ключевую ставку) на 200 базисных пунктов до 9,00 процента. Решение вступает в силу с 28 мая 2024 года."
        )
