from django.shortcuts import render, get_object_or_404
from .models import *
from django.http import JsonResponse

# Create your views here.


def home(request):
    boards = Board.objects.all()
    data = {'results': list(boards.values("pk", "name", "description"))}
    return JsonResponse(data)


def board_topics(request, board_id):
    board = get_object_or_404(Board, pk=board_id)
    data = {'results': {"name": board.name, "description": board.description}}
    return JsonResponse(data)
