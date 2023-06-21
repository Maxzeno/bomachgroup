from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings


def send_email_quote(email, quote_model):
	if not isinstance(email, list):
		email = list(email)
	subject = 'New User wants Project Estimate'
	message = f"""Name: {quote_model.name}
Phone number:{quote_model.phone}
Email:{quote_model.email}
Location:{quote_model.location}
Service:{quote_model.service.name}
Sub Service:{quote_model.sub_service.name}
Message:{quote_model.message}
"""
	send_mail(subject, message, settings.EMAIL_HOST_USER, email, fail_silently=False)
