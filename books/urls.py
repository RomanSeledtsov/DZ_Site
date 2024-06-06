from django.urls import path
from books import views

urlpatterns = [
    path('books/', views.books_list_view),
    path('books/<int:id>/', views.books_detail_view),




    path('name/', views.name_view),
    path('bio/', views.bio_view),
    path('datetime/', views.datetime_view),
    path('count/', views.count_view),
]