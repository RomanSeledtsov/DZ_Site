from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from . import models


# Adventure tag

def advent_tag_view(request):
    if request.method == 'GET':
        advents_tags = models.MyBooks.objects.filter(tags__name="Приключения").order_by('-id')
        return render(
            request,
            template_name='my_books/advents_tags.html',
            context={'advents_tags': advents_tags}
        )


# My books

def all_books(request):
    if request.method == "GET":
        books = models.MyBooks.objects.filter().order_by('-id')
        return render(
            request,
            template_name='my_books/all_books.html',
            context={
                'books': books
            }
        )


# Book detail
def books_detail_view(request, id):
    if request.method == 'GET':
        book_id = get_object_or_404(models.Books, id=id)
        return render(
            request,
            template_name="books/books_detail.html",
            context={
                "book_id": book_id
            }
        )


# Book list

def books_list_view(request):
    if request.method == "GET":
        queryset = models.Books.objects.filter().order_by('-id')
        return render(
            request,
            template_name='books/books_list.html',
            context={
                'book': queryset
            }
        )


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
