import os
from celery import Celery  #импортируем библиотеку для взаимодействия с операционной системой и саму библиотеку Celery.
from celery.schedules import crontab

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings') #связываем настройки Django с настройками Celery через переменную окружения.

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY') # создаем экземпляр приложения Celery и устанавливаем для него файл конфигурации

app.autodiscover_tasks() #указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.

app.conf.beat_schedule = {
    'send_mail_every_monday_8am': {
        'task': 'NewsPaper.tasks.send_mail_weekly',
        'schedule': crontab(hour=8, minute=0, day_of_week='monday'),
    },
}