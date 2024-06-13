from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from . import models, forms
from .forms import BookForm


# CRUD UPDATE-DELETE-READ-CREATE

# edit book

def edit_book_view(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    if request.method == 'POST':
        form = forms.BookForm(request.POST, instance=book_id)
        form.save()
        return HttpResponse('<h3>Book Edited!</h3>'
                            '<a href="/books/">Список книг</a>')
    else:
        form = forms.BookForm(instance=book_id)
    return render(
        request,
        template_name='books/edit_book.html',
        context={
            'form': form,
            'book_id': book_id
        }
    )


# delete book
def drop_book_view(request, id):
    book_id = get_object_or_404(models.Books, id=id)
    book_id.delete()
    return HttpResponse('<h3>Book Deleted!</h3>'
                        '<a href="/books/">Список книг</a>')


# create book
def create_book_view(request):
    if request.method == 'POST':
        form = forms.BookForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return HttpResponse('<h3>Book Created!</h3>'
                                '<a href="/books/">Список книг</a>')
    else:
        form = forms.BookForm()
    return render(
        request,
        template_name='books/create_book.html',
        context={'form': form}
    )


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
