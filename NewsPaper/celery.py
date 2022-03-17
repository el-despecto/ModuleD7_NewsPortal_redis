import os
from celery import Celery #импортируем библиотеку для взаимодействия с операционной системой и саму библиотеку Celery.

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'NewsPaper.settings') #связываем настройки Django с настройками Celery через переменную окружения.

app = Celery('NewsPaper')
app.config_from_object('django.conf:settings', namespace='CELERY') # создаем экземпляр приложения Celery и устанавливаем для него файл конфигурации

app.autodiscover_tasks() #указываем Celery автоматически искать задания в файлах tasks.py каждого приложения проекта.