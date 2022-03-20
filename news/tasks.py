from celery import shared_task
from django.core.mail import EmailMultiAlternatives
from celery.schedules import crontab


@shared_task
def send_mail(sub_username, sub_useremail, html_content):
    msg = EmailMultiAlternatives(
        subject=f'Здравствуйте, {sub_username}. Новая статья в вашем разделе!',
        from_email='d3spector@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')
    print(html_content)
    print()
    msg.send()

@shared_task
def send_mail_weekly(sub_username, sub_useremail, html_content):

    msg = EmailMultiAlternatives(
        subject=f'Здравствуйте, {sub_username}, новые статьи за прошлую неделю',
        from_email='d3spector@yandex.ru',
        to=[sub_useremail]
    )

    msg.attach_alternative(html_content, 'text/html')
    print(html_content)
    msg.send()


