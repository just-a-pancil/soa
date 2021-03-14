import os

from celery import Celery
from celery.schedules import crontab

# set the default Django settings module for the 'celery' program.
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'soa.settings')

app = Celery(
            'soa',
            include=['soa.tasks']
            )

# Using a string here means the worker doesn't have to serialize
# the configuration object to child processes.
# - namespace='CELERY' means all celery-related configuration keys
#   should have a `CELERY_` prefix.
app.config_from_object('django.conf:settings', namespace='CELERY')

# Load task modules from all registered Django app configs.
app.autodiscover_tasks()


@app.task(bind=True)
def debug_task(self):
    print(f'Request: {self.request!r}')

app.conf.beat_schedule = {
    'every-day-23-00': {
        # here must be task 'name' param
        'task': 'key_cleaner',  
        # according to london TIME_ZONE (at 20:00 in london we having 23:00)
        'schedule': crontab(hour='20', minute='0', day_of_week='*', ),
    },
    # #Scheduler Name
    # 'every-shth': {
    #     # Task Name (Name Specified in Decorator)
    #     'task': 'print-Cleaner-is-HERE!!!!',  
    #     # Schedule      
    #     'schedule': 5,
    #     # Function Arguments 
    #     # 'args': ("Hello",) 
    # },
}


# ./redis-stable/src/redis-server 
# celery -A soa.celery beat -El INFO
# celery -A soa.celery worker -El INFO
