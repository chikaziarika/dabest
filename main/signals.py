from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

from django.core.mail import send_mail

@receiver(post_save, sender=User)
def send_email_to_admin(sender, instance, created, **kwargs):
    if created:
        send_mail(
            '<Subject>User {} has been created'.format(instance.username),
            '<Body>A new user has been created',
            'from@example.com',
            ['admin@dabestconsultant.com'],
            fail_silently=False,
        )

