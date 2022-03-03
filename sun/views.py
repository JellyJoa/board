from django.shortcuts import render, redirect, get_object_or_404
from sun.models import Board
from sun.form import BoardForm, BoardDetailForm
# Create your views here.

def b_tip(request):
    if request.user.is_authenticated:
        posts = Board.objects.all().order_by('-id')
        context = {
            'posts' : posts
        }
        return render(request, 'tip.html', context)
    else:
        return redirect('home')

def create(request):
    if request.method == 'GET':
        board_form = BoardForm()
        context = {
            'my_form': board_form
        }
        return render(request, 'create.html', context)
    else:
        board_form = BoardForm(request.POST)
        if board_form.is_valid():
            board_form.save()

            return redirect('sun:b_tip')

def b_detail(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    board_detail_form = BoardDetailForm(instance=post)
    comments = post.comment_set.all().order_by('-id')
    context = {
        'detail_form': board_detail_form,
        'comments': comments
    }
    return render(request, 'detail.html', context)