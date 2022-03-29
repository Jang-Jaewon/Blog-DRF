from django.urls import path, include

from rest_framework import routers

from api import views


router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('posts/', views.PostViewSet.as_view(actions={'get' : 'list', 'post' : 'create'}), name='post-list'),
    path('posts/<int:pk>/', views.PostViewSet.as_view(actions={'get' : 'retrieve', 'patch' : 'partial_update', 'delete' : 'destroy'}), name='post-detail'),
    path('posts/<int:pk>/like/', views.PostViewSet.as_view(actions={'get' : 'like',}), name='post-like'),
    path('comments/', views.CommentViewSet.as_view(actions={'get' : 'list', 'post' : 'create'}), name='comment-create'),
    path('catetag/', views.CateTagAPIView.as_view(), name='catetag'),
]