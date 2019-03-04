from django.shortcuts import render, get_object_or_404, redirect

from boards.models import Board, User, Topic, Post
from boards.forms import NewTopicForm


def home(request):
    boards = Board.objects.all()
    return render(request, 'home.html', {'boards': boards})


def board_topics(request, pk):
    board = get_object_or_404(Board, pk=pk)
    return render(request, 'topics.html', {'board': board})


def new_topic(request, pk):
    board = get_object_or_404(Board, pk=pk)
    user = User.objects.first()

    if request.method == 'POST':
        form = NewTopicForm(request.POST)

        # 验证form是否有效
        if form.is_valid():
            # 将数据保存至数据库 Topic, 并返回Topic的实例对象
            topic = form.save(commit=False)
            # 对返回的Topic实例对象修改后重新保存
            topic.board = board
            topic.starter = user
            topic.save()

            Post.objects.create(message=form.cleaned_data.get('message'),
                                topic=topic,
                                created_by=user)
            return redirect('board_topics', pk=board.pk)
    # 'GET'
    else:
        # 初始化一个新的空表单
        form = NewTopicForm()

    return render(request, 'new_topic.html', {'board': board, 'form': form})
