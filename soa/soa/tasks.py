from django.contrib.auth.models import User, Group
from celery import shared_task

from .celery import app

# i'll need it later
    #     crontab(hour='23', minute='0', day_of_week='*', ),


@shared_task(name='print-Cleaner-is-HERE!!!!')
def print_cleaner():
    print('Cleaner is HERE!!!!')

@shared_task(name='key_cleaner')
def key_cleaner():
    print('Cleaner is HERE!!!!')
    from newKey.models import Keys
    # deleted = 0
    for key in Keys.objects.all():
        if not key.is_valid():
            deleted += 1
            key.__clear_self__()
            key.delete()
    # print(f'Cleaner is going to sleep !!! There are {deleted} killed')
    return