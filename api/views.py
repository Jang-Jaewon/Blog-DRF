from django.contrib.auth.models import User

from rest_framework          import viewsets
from rest_framework          import generics
from rest_framework          import views
from rest_framework.response import Response

from api         import serializers, pagination
from blog.models import Post, Comment, Category, Tag


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostListAPIView(generics.ListCreateAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer
    pagination_class = pagination.PostPageNumberPagination
    
    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }


# class PostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
#     queryset = Post.objects.all()
#     serializer_class = serializers.PostRetrieveSerializer


def get_prev_next_instance(instance):
    try:
        prev_intance = instance.get_previous_by_update_dt()
    except instance.DoesNotExist:
        prev_intance = None
    try:
        next_intance = instance.get_next_by_update_dt()
    except instance.DoesNotExist:
        next_intance = None
    return prev_intance, next_intance
        
        
class PostRetrieveAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Post.objects.all()
    serializer_class = serializers.PostDetailSerializer
    
    def retrieve(self, request, *args, **kwargs):
        instance     = self.get_object()
        prevInstance, nextInstance = get_prev_next_instance(instance)
        commentList  = instance.comment_set.all()
        data = {
            'post'        : instance,
            'prevPost'    : prevInstance,
            'nextPost'    : nextInstance,
            'commentlist' : commentList,
        }
        serializer = self.get_serializer(instance=data)
        return Response(serializer.data)


class CommentCreateAPIView(generics.ListCreateAPIView):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer
    

class PostLikeAPIView(generics.GenericAPIView):
    queryset = Post.objects.all()
    
    def get(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)
        

class CateTagAPIView(views.APIView):
    def get(self, request, *args, **kwargs):
        cateList = Category.objects.all()
        tagList  = Tag.objects.all()
        data = {
            'cateList' : cateList,
            'tagList' : tagList,
        }
        
        serializer = serializers.CateTagSerializer(instance=data)
        return Response(serializer.data)