from rest_framework import serializers
from .models import Bookmark

class BookmarkSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bookmark
        fields = ('id', 'url', 'title', 'description', 'codeblock', 'created_at', 'modified_at')
