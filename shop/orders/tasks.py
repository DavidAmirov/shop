from celery import shared_task

from django.core.mail import send_mail

from .models import Order


@shared_task
def order_created(order_id):
    '''Задание CELERY по отправке сообщения при успешном создании заказа.'''
    order = Order.objects.get(id=order_id)
    subject = f'Заказ №{order.id}'
    message = f'Уважаемый {order.first_name} ваш заказ №{order.id} оформлен.'
    mail_sent = send_mail(subject, message, 'admin@mail.ru', [order.email])
    return mail_sent