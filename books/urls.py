from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BookViewSet, UserViewSet

router = DefaultRouter()
router.register('books', BookViewSet, basename='book_management')
router.register('users',UserViewSet, basename='user_management')
urlpatterns = [
    path('',include(router.urls))
]
