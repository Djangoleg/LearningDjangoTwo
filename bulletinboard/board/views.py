from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from board.models import Bb


def index(request):
    bbs = Bb.objects.order_by('-published')
    title = 'Список объявлений'
    context = {'bbs': bbs, 'title': title}

    return render(request=request, template_name='index.html', context=context)
