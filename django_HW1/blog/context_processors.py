import datetime


def shared_context(request):
    return {
        'year': datetime.datetime.today().year
    }
