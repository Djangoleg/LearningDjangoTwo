from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from board.models import Bb


def index(request):
    title = 'Список объявлений\r\n\r\n\r\n'

    for x in Bb.objects.order_by('-published'):
        title += f'{x.title}\r\n{x.content}\r\n\r\n'

    return HttpResponse(title, content_type='text/plain; charset=utf-8')