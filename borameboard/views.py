from borameboard.models import Board
from django.shortcuts import render,redirect
from .models import Board
from .forms import RegistForm
from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render, get_object_or_404
from .forms import *
from .models import *
from django.contrib.auth.models import User

def index(request):
    page = request.GET.get('page', '1')  # 페이지 파라미터 얻기, 없으면 1
    board_list = Board.objects.order_by('-id')

    # 페이징 처리
    paginator = Paginator(board_list, 10)  # 페이지당 10개씩 보여주기
    page_obj = paginator.get_page(page)  # page에 해당하는 페이징 객체 생성
    user = request.user
    context = {'board_list': page_obj,
               'user':user
               }   # 페이징 객체(page_obj) 전달
    return render(request, 'borameboard/index.html', context)



def regist(request):
    if request.method == 'POST':
        form = RegistForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('borame_board:index')
    else:
        form = RegistForm()
    context = {'form': form,
               'user': request.user}
    return render(request, 'borameboard/regist_form.html', context)

def detail(request, pk):
    board_list = get_object_or_404(Board, id=pk)
    context = {'board_list': board_list}
    return render(request, 'borameboard/detail.html', context)

def edit(request, pk):
    post = get_object_or_404(Board, id=pk)
    if request.method == 'POST':
        form = RegistForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save()
            return redirect('borame_board:index')
    else:
        form = RegistForm(instance=post)
    context = {'form': form,}
    return render(request, 'borameboard/edit_form.html', context)

def delete(request, pk):
    post = get_object_or_404(Board, id=pk)
    post.delete()
    return redirect('borame_board:index')