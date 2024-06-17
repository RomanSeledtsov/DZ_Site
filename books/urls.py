from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.AllBooks.as_view()),
    path('advents_tags/', views.AdventTagView.as_view()),


    path('books/', views.BooksListView.as_view(), name='books'),
    path('books/<int:id>/', views.BooksDetailView.as_view()),
    path('books/<int:id>/delete', views.DeleteBookView.as_view()),
    path('books/<int:id>/update', views.EditBooksView.as_view()),
    path('create_book/', views.CreateBookView.as_view()),
    path('search/', views.SearchView.as_view(), name='search'),




    # path('name/', views.name_view),
    # path('bio/', views.bio_view),
    # path('datetime/', views.datetime_view),
    # path('count/', views.count_view),
]