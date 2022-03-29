from django.contrib.auth.models import User

from rest_framework          import viewsets
from rest_framework          import generics
from rest_framework          import views
from rest_framework.response import Response

from api         import serializers, pagination, utils
from blog.models import Post, Comment, Category, Tag


class UserViewSet(viewsets.ModelViewSet):
    queryset = User.objects.all()
    serializer_class = serializers.UserSerializer


class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all()
    serializer_class = serializers.PostListSerializer
    pagination_class = pagination.PostPageNumberPagination
    
    def get_serializer_context(self):
        return {
            'request': None,
            'format': self.format_kwarg,
            'view': self
        }
    
    def get_queryset(self):
        return Post.objects.all().select_related('category').prefetch_related('tags', 'comment_set')

    def retrieve(self, request, *args, **kwargs):
        instance = self.get_object()
        commentList = instance.comment_set.all()

        postDict = utils.obj_to_post(instance)
        prevDict, nextDict = utils.prev_next_post(instance)
        commentDict = [utils.obj_to_comment(c) for c in commentList]

        dataDict = {
            'post': postDict,
            'prevPost': prevDict,
            'nextPost': nextDict,
            'commentList': commentDict,
        }

        return Response(dataDict)

    def like(self, request, *args, **kwargs):
        instance = self.get_object()
        instance.like += 1
        instance.save()
        return Response(instance.like)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all()
    serializer_class = serializers.CommentSerializer

    
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