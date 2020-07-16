from django.db import models
from django.urls import reverse


class Book(models.Model):
    title = models.CharField(max_length=200)
    author = models.CharField(max_length=100)
    description = models.TextField(max_length=1000, help_text="Enter a brief description of the book")
    id = models.AutoField(primary_key=True, help_text="Unique ID for this particular book across whole library")

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('book-detail', args=[str(self.id)])
