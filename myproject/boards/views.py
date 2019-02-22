from django.http import HttpResponse

from boards.models import Board


def home(request):
    boards = Board.objects.all()
    board_names = list()

    for board in boards:
        board_names.append(board.name)

    response_html = '<br>'.join(board_names)

    return HttpResponse(response_html)
