from django.dispatch import receiver
from django.core.mail import send_mail
from django.db.models.signals import post_save

from emails.models import EmailSchedule


@receiver(post_save, sender="users.User")
def send_welcome_email(sender, instance, created, **kwargs):
    if created:
        EmailSchedule.objects.create(
            to_email=instance.email,
            to_name=instance.name,
            subject='Welcome to our platform',
            body='Welcome to our platform',
            from_email='info@example.com',
            from_name='Example Team',
        )