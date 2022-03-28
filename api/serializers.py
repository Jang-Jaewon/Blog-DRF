from django.contrib.auth.models import User

from rest_framework import serializers

from blog.models import Post, Comment

class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'is_staff']
        

class PostListSerializer(serializers.ModelSerializer):
    category = serializers.CharField(source='category.name')
    
    class Meta:
        model = Post
        fields = ['id', 'title', 'image', 'like', 'category']
        
        
class PostRetrieveSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        exclude = ['create_dt']


class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Comment
        fields = '__all__'


class CateTagSerializer(serializers.Serializer):
    cateList = serializers.ListField(child=serializers.CharField())
    tagList  = serializers.ListField(child=serializers.CharField())
    