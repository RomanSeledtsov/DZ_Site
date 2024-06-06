from django.urls import path
from books import views

urlpatterns = [
    path('name/', views.name_view),
    path('bio/', views.bio_view),
    path('datetime/', views.datetime_view),
    path('count/', views.count_view),
    ]