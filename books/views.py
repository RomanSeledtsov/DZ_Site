from django.shortcuts import render, get_object_or_404
from django.http import HttpResponse
from datetime import datetime
import random
from . import models, forms
from .forms import BookForm
from django.views import generic


# Search button


class SearchView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "book"
    paginate_by = 5

    def get_queryset(self):
        return models.Books.objects.filter(
            name__icontains=self.request.GET.get("q")
        ).order_by("-id")

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context["q"] = self.request.GET.get("q")
        return context


# CRUD UPDATE-DELETE-READ-CREATE


# Edit book
class EditBooksView(generic.UpdateView):
    template_name = "books/edit_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(EditBooksView, self).form_valid(form=form)


# Delete book
class DeleteBookView(generic.DeleteView):
    template_name = "books/confirm_delete.html"
    success_url = "/books/"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)


# Create book
class CreateBookView(generic.CreateView):
    template_name = "books/create_book.html"
    form_class = forms.BookForm
    success_url = "/books/"

    def form_valid(self, form):
        print(form.cleaned_data)
        return super(CreateBookView, self).form_valid(form=form)


# Adventure tag
class AdventTagView(generic.ListView):
    template_name = "my_books/advents_tags.html"
    context_object_name = "advents_tags"

    def get_queryset(self):
        return models.MyBooks.objects.filter(tags__name="Приключения").order_by("-id")


# My books
class AllBooks(generic.ListView):
    template_name = "my_books/all_books.html"
    context_object_name = "books"

    def get_queryset(self):
        return models.MyBooks.objects.filter().order_by("-id")


# Book detail


class BooksDetailView(generic.DetailView):
    template_name = "books/books_detail.html"
    context_object_name = "book_id"

    def get_object(self, **kwargs):
        book_id = self.kwargs.get("id")
        return get_object_or_404(models.Books, id=book_id)


# Book list


class BooksListView(generic.ListView):
    template_name = "books/books_list.html"
    context_object_name = "book"
    model = models.Books
    ordering = ["-id"]

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["quote"] = models.Quote.objects.filter().order_by("-id")
        return context


# def edit_book_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, instance=book_id)
#         form.save()
#         return HttpResponse('<h3>Book Edited!</h3>'
#                             '<a href="/books/">Список книг</a>')
#     else:
#         form = forms.BookForm(instance=book_id)
#     return render(
#         request,
#         template_name='books/edit_book.html',
#         context={
#             'form': form,
#             'book_id': book_id
#         }
#     )


# def get_queryset(self):
#     return self.models.objects.filter().order_by('-id')

# def books_list_view(request):
#     if request.method == "GET":
#         queryset = models.Books.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='books/books_list.html',
#             context={
#                 'book': queryset
#             }
#         )


# def name_view(request):
#     if request.method == "GET":
#         return HttpResponse('Привет, меня зовут Селедцов Роман, мне 25')
#
#
# def bio_view(request):
#     if request.method == "GET":
#         return HttpResponse('Увлекаюсь программированием, историей, компиком 😏 и т.д')
#
#
# def datetime_view(request):
#     if request.method == "GET":
#         date_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
#         return HttpResponse(f'Местное время {date_time} ⌛')
#
#
# def count_view(request):
#     if request.method == "GET":
#         random_num = random.randint(1, 50)
#         return HttpResponse(f'Твое случайное число {random_num} 🔢')


# def books_detail_view(request, id):
#     if request.method == 'GET':
#         book_id = get_object_or_404(models.Books, id=id)
#         return render(
#             request,
#             template_name="books/books_detail.html",
#             context={
#                 "book_id": book_id
#             }
#         )

# def all_books(request):
#     if request.method == "GET":
#         books = models.MyBooks.objects.filter().order_by('-id')
#         return render(
#             request,
#             template_name='my_books/all_books.html',
#             context={
#                 'books': books
#             }
#         )

# def advent_tag_view(request):
#     if request.method == 'GET':
#         advents_tags = models.MyBooks.objects.filter(tags__name="Приключения").order_by('-id')
#         return render(
#             request,
#             template_name='my_books/advents_tags.html',
#             context={'advents_tags': advents_tags}
#         )


# def create_book_view(request):
#     if request.method == 'POST':
#         form = forms.BookForm(request.POST, request.FILES)
#         if form.is_valid():
#             form.save()
#             return HttpResponse('<h3>Book Created!</h3>'
#                                 '<a href="/books/">Список книг</a>')
#     else:
#         form = forms.BookForm()
#     return render(
#         request,
#         template_name='books/create_book.html',
#         context={'form': form}
#     )

# def drop_book_view(request, id):
#     book_id = get_object_or_404(models.Books, id=id)
#     book_id.delete()
#     return HttpResponse('<h3>Book Deleted!</h3>'
#                         '<a href="/books/">Список книг</a>')
