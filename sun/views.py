from django.shortcuts import render, redirect, get_object_or_404
from sun.models import Board, Comment
from sun.form import BoardForm, BoardDetailForm
from django.http import JsonResponse
# import requests
# import json
# from django.http import HttpResponseRedirect
# Create your views here.

def b_tip(request):
    # if request.user.is_authenticated:
    #     posts = Board.objects.all().order_by('-id')
    #     context = {
    #         'posts': posts
    #     }
    #     return render(request, 'tip.html', context)
    # else:
    #     return redirect('home')
    posts = Board.objects.all().order_by('-id')
    context = {
        'posts': posts
    }
    return render(request, 'tip.html', context)

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

def b_delete(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    post.delete()
    return redirect('sun:b_tip')

def b_edit(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    if request.method == 'POST':
        board_form = BoardForm(request.POST, request.FILES)
        if board_form.is_valid():
            print(board_form.cleaned_data)
            post.b_title = board_form.cleaned_data['b_title']
            post.b_author = board_form.cleaned_data['b_author']
            post.b_content = board_form.cleaned_data['b_content']
            board_form.save()
            return redirect('/sun/'+ str(board_id) +'/detail/')
    else:
        board_form = BoardForm(instance=post)
        context = {
            'board_form': board_form,
            'writing': True,
            'now': 'edit'
        }
        return render(request, 'edit.html', context)

def b_like(request, board_id):
    post = get_object_or_404(Board, pk=board_id)
    post.b_like_count += 1
    post.save()

    board_detail_form = BoardDetailForm(instance=post)

    context = {
        'detail_form': board_detail_form
    }
    return render(request, 'detail.html', context)

def c_create(request):
    comment = Comment()
    comment.c_author = request.GET['comment_author']
    comment.c_content = request.GET['comment_content']
    comment.c_date = request.GET['comment_date']
    comment.board_id = request.GET['board_id']
    comment.save()

    post = get_object_or_404(Board, pk=request.GET['board_id'])
    post.b_comment_count += 1
    post.save()

    return JsonResponse({
        'c_id': comment.id,
        'c_author': comment.c_author,
        'c_content': comment.c_content,
        'c_date': comment.c_date
    }, json_dumps_params={'ensure_ascii': True})

def c_delete(request):
    comment = get_object_or_404(Comment, pk=request.GET['comment_id'])
    comment.delete()

    post = get_object_or_404(Board, pk=request.GET['board_id'])
    post.b_comment_count -= 1
    post.save()

    return JsonResponse({}, json_dumps_params={'ensure_ascii': True})

# def adopt(request):
#     url = ''
#     res = requests.get(url)
#     text = res.text
#
#     d = json.loads(text)
#
#     return render(request, 'adopt.html')