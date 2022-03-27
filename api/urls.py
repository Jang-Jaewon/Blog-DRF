from django.urls import path, include

from rest_framework import routers

from api.views import UserViewSet, PostViewSet, CommentViewSet


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'posts', PostViewSet)
router.register(r'comments', CommentViewSet)

urlpatterns = [
    path('', include(router.urls)),
]