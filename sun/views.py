from django.shortcuts import render
from sun.models import Board
# Create your views here.

def b_tip(request):
    posts = Board.objects.all().order_by('-id')
    context = {
        'posts' : posts
    }

    return render(request, 'tip.html', context)