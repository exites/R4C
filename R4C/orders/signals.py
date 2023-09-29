from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from django.template.loader import render_to_string
from django.conf import settings


from .models import Order
from robots.models import Robot

@receiver(post_save, sender=Robot)
def check_robot_availability(sender, instance, created, **kwargs):
    if created:
        try:
            order = Order.objects.get(robot_serial=instance.serial)
            send_robot_available_notification(order)
        except Order.DoesNotExist:
            pass

def send_robot_available_notification(order):
    try:
        robot = Robot.objects.get(serial=order.robot_serial)
    except Robot.DoesNotExist:
        robot = None

    if robot:
        subject = 'Робот доступен'
        message = render_to_string('orders/email_notification.html', {
            'model': robot.model,
            'version': robot.version
        })
        from_email = settings.DEFAULT_FROM_EMAIL
        to = order.customer.email
        recipient_list = [to]

        send_mail(subject, message, from_email, recipient_list, html_message=message)