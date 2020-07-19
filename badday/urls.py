from django.urls import path

from badday.views import *



app_name = "books"

urlpatterns = [
    path('v1/books/', BookViewSet.as_view({'get':'list'})),
    path('v1/books/<int:id>/', BookViewSet.as_view({'get':'book_id'})),
    path('v1/books/create/', BookCreateView.as_view()),
    path('v1/books/detail/<int:pk>/', BookDetailView.as_view())
]

