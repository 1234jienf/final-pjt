from django.shortcuts import render
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

# permission Decorators
from rest_framework.decorators import permission_classes
from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly

from .serializers import BoardListSerializer, BoardSerializer, CommentSerializer
from .models import Board, Comment
# Create your views here.
from django.shortcuts import render, redirect, get_object_or_404, get_list_or_404
from .forms import BoardForm, CommentForm
from django.views.decorators.http import require_http_methods
from django.contrib.auth.decorators import login_required



# Create your views here.

@api_view(['GET','POST'])
@permission_classes([IsAuthenticated])
def index(request):
    if request.method == 'GET':
        boards = Board.objects.all()
        serializer = BoardListSerializer(boards, many=True)
        return Response(serializer.data)
    
    elif request.method == 'POST':
            serializer = BoardSerializer(data=request.data)
            if serializer.is_valid(raise_exception=True):
                serializer.save(author=request.user)
                return Response(serializer.data, status=status.HTTP_201_CREATED)
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)



@api_view(['GET'])
def detail(request, pk):
    try:
        board = Board.objects.get(pk=pk)
    except Board.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    serializer = BoardSerializer(board)
    return Response(serializer.data)


@api_view([ 'DELETE'])
@permission_classes([IsAuthenticated])
def delete(request, pk):
    board = get_object_or_404(Board, pk=pk)

    if board.author == request.user:
        board.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
        

@api_view(['PUT'])
@permission_classes([IsAuthenticated])
def update(request, pk):
    board = get_object_or_404(Board, pk=pk)

    serializer = BoardSerializer(board, data=request.data)
    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_200_OK)
    return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    

@api_view(['GET', 'POST'])
@permission_classes([IsAuthenticatedOrReadOnly])
def comment(request, board_pk):
    board = get_object_or_404(Board, pk=board_pk)
    
    if request.method == 'GET':
        comments = Comment.objects.filter(board=board)
        serializer = CommentSerializer(comments, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    elif request.method == 'POST':
        serializer = CommentSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(board=board, author=request.user)
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def comment_detail(request, board_pk, comment_pk):
    comment = get_object_or_404(Comment, pk=comment_pk)
    
    if comment.author == request.user:  # 댓글 작성자와 현재 로그인한 사용자를 비교
        comment.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    else:
        return Response("권한이 없습니다.", status=status.HTTP_403_FORBIDDEN)
    

# @login_required
# @require_http_methods(["POST"])
# def comment(request, board_pk):
#     board = get_object_or_404(Board, pk=board_pk)
#     if request.method == 'POST':
#         form = CommentForm(request.POST)
#         if form.is_valid():
#             comment = form.save(commit=False)
#             comment.board = board
#             comment.save()
#             return redirect('boards:detail', board.pk)


# @require_http_methods(["POST"])
# def comment_detail(request, board_pk, comment_pk):
#     comment = get_object_or_404(Comment, pk=comment_pk)
#     if request.method == 'POST':
#         comment.delete()
#         return redirect('boards:detail', board_pk)
    

# def likes(request, article_pk):
#     article = Board.objects.get(pk=article_pk)
#     if request.user in article.like_users.all():
#         article.like_users.remove(request.user)
#     else:
#         article.like_users.add(request.user)
#     return redirect('boards:index')