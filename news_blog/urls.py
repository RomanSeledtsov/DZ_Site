from django.urls import path
from news_blog import views

urlpatterns = [
    path('hello/', views.hello_view),
    path('news/', views.news_view),
]
