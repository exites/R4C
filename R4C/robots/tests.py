from django.test import TestCase
from django.core import mail
from .models import Robot
from customers.models import Customer

class RobotNotificationTests(TestCase):
    def test_robot_notification_email(self):
        # Create a customer
        customer = Customer.objects.create(email='test@example.com')

        # Create a robot
        robot = Robot.objects.create(model='TestModel', version='V1')

        # Manually trigger the signal
        robot.save()

        # Check the email was sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].subject, 'Robot Availability Notification')
        self.assertIn('TestModel', mail.outbox[0].body)
        self.assertIn('V1', mail.outbox[0].body)
        self.assertIn('test@example.com', mail.outbox[0].to)