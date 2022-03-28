from django.urls import path, include

from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostListAPIView.as_view(), name='post-list'),
    path('posts/<int:pk>/', views.PostRetrieveAPIView.as_view(), name='post-detail'),
    path('posts/<int:pk>/like/', views.PostLikeAPIView.as_view(), name='post-like'),
    path('comments/', views.CommentCreateAPIView.as_view(), name='comment-create'),
    path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),
]