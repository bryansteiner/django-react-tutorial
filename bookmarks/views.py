from .models import Bookmark
from .serializers import BookmarkSerializer
from rest_framework import generics

# Create your views here.
class BookmarkListCreate(generics.ListCreateAPIView):
    queryset = Bookmark.objects.all()
    serializer_class = BookmarkSerializer
