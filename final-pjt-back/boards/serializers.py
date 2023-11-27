from rest_framework import serializers
from .models import Board, Comment

class BoardListSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')  # Get the username through the ForeignKey

    class Meta:
        model = Board
        fields = ('id', 'username', 'title', 'content')

class CommentSerializer(serializers.ModelSerializer):
    username = serializers.ReadOnlyField(source='author.username')

    class Meta:
        model = Comment
        fields = ('id', 'username', 'content', 'created_at', 'updated_at')

class BoardSerializer(serializers.ModelSerializer):

    author_username = serializers.ReadOnlyField(source='author.username')
    comments = CommentSerializer(many=True, read_only=True)
    
    class Meta:
        model = Board
        fields = '__all__'
        read_only_fields = ('author',)

