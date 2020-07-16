from django.urls import path

from badday.views import *



app_name = "books"

urlpatterns = [
    path('books/', BookView.as_view()),
    path('books/<int:id>/', Bookbyid.as_view()),
    path('books/create/', BookCreateView.as_view()),
    path('books/detail/<int:pk>/', BookDetailView.as_view())
]
