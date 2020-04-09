from django.urls import path
from . import views

urlpatterns = [
    path('api/bookmark/', views.BookmarkListCreate.as_view() ),
]
