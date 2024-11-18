from django.core.mail import send_mail
import sys
from pathlib import Path
sys.path.append(Path(__file__).resolve().parent.parent.__str__())
print (sys.path)
import os
os.environ.setdefault("DJANGO_SETTINGS_MODULE", "dabest.settings")

import django
django.setup()

from django.core.management import call_command

subject = 'Test Email Untuk Ke 2'
message = 'This is a test email sent using SMTP in Django.'
from_email = 'admin@dabestconsultant.com'
recipient_list = ['tazsafakhri@gmail.com']

send_mail(subject, message, from_email, recipient_list)