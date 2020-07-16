from rest_framework import serializers

from badday.models import Book


class BookSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    author = serializers.CharField()
    id = serializers.CharField()

class BookbyidSerializer(serializers.Serializer):
    title = serializers.CharField(max_length=120)
    description = serializers.CharField()
    author = serializers.CharField()

class BookDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Book
        fields = ('title', 'description', 'author')
