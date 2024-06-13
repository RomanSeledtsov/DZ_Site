from django.urls import path
from . import views

urlpatterns = [
    path('all_books/', views.all_books),
    path('advents_tags/', views.advent_tag_view),


    path('books/', views.books_list_view),
    path('books/<int:id>/', views.books_detail_view),
    path('books/<int:id>/delete', views.drop_book_view),
    path('books/<int:id>/update', views.edit_book_view),
    path('create_book/', views.create_book_view),




    path('name/', views.name_view),
    path('bio/', views.bio_view),
    path('datetime/', views.datetime_view),
    path('count/', views.count_view),
]