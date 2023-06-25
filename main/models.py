from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import post_save, pre_save
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField
import bleach
from .utils import (
    send_email_quote, send_email_contact, send_booking_email, send_user_booking_email, unique_id)

# Create your models here.


class ImageUrl:
    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/assets/img/logo/bomach-logo-hd.jpeg'


class CustomBaseModel:
    def short_content(self):
        if self.content:
            rich_text = self.content.replace('&nbsp;', '')
            text = bleach.clean(rich_text, tags=[], strip=True)
            cleaned_string = ' '.join(list(text.split()))
            return f"{cleaned_string[:50]}.."
        return ''


class Service(models.Model, ImageUrl, CustomBaseModel):
    name = models.CharField(max_length=500, unique=True)
    slug = models.CharField(max_length=500, unique=True, blank=True)
    image = models.ImageField(upload_to='images/')
    content = RichTextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Value cannot be less than 0.'),
            MaxValueValidator(100, message='Value cannot be greater than 100.')
        ],
        default=80) # ranting over 100%
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class SubService(models.Model, ImageUrl, CustomBaseModel):
    name = models.CharField(max_length=500, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=500, unique=True, blank=True)
    image = models.ImageField(upload_to='images/')
    content = RichTextField()
    rating = models.IntegerField(
        validators=[
            MinValueValidator(0, message='Value cannot be less than 0.'),
            MaxValueValidator(100, message='Value cannot be greater than 100.')
        ],
        default=80) # ranting over 100%
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Project(models.Model, ImageUrl, CustomBaseModel):
    name = models.CharField(max_length=500, null=True, blank=True)
    slug = models.CharField(max_length=500, unique=True, blank=True)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, null=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    min_budget = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    feedback = models.CharField(max_length=500, null=True, blank=True,)
    content = RichTextUploadingField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class ProductImage(models.Model, ImageUrl):
    name = models.CharField(max_length=1000, default='N/A')
    priority = models.IntegerField(default=0)
    image = models.ImageField(upload_to='images/')
    date = models.DateTimeField(default=timezone.now)


def product_id():
    return unique_id(Product)

class Product(models.Model, CustomBaseModel):
    id = models.CharField(primary_key=True, max_length=6, default=product_id) # to be added
    name = models.CharField(max_length=1000)
    # description = models.TextField(max_length=100000)
    slug = models.CharField(max_length=500, unique=True, blank=True)
    content = RichTextUploadingField()
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True, blank=True)
    video = models.FileField(upload_to='video/', null=True, blank=True)
    # image = models.ImageField(upload_to='images/') # to be removed
    product_images = models.ManyToManyField(ProductImage) # to be added
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def video_url(self):
        if self.video:
            return self.video.url
        return ''

    def image_url(self):
        product_image = self.product_images.order_by('-priority').first()
        if product_image:
            return product_image.image_url()
        return '/static/assets/img/logo/bomach-logo-full.jpeg'

    def __str__(self):
        return self.name


class Blog(models.Model, ImageUrl, CustomBaseModel):
    title = models.CharField(max_length=500, null=True, blank=True)
    author = models.CharField(max_length=500, null=True, blank=True)
    slug = models.CharField(max_length=500, unique=True, blank=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title


class HomeSlider(models.Model, ImageUrl):
    # title = models.CharField(max_length=500)
    big_text = models.CharField(max_length=500)
    small_text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.big_text


class CustomerReview(models.Model):
    name = models.CharField(max_length=500)
    review = models.CharField(max_length=2000)
    occupation = models.CharField(max_length=500)
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class Employee(models.Model, ImageUrl):
    name = models.CharField(max_length=500)
    job_title = models.CharField(max_length=500)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name


class PartnerSlider(models.Model, ImageUrl):
    company = models.CharField(max_length=500, default="N/A")
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.company


class Quote(models.Model):
    name = models.CharField(max_length=500, default="N/A")
    phone = models.CharField(max_length=500, default="N/A")
    email = models.CharField(max_length=500, default="N/A")
    message = models.CharField(max_length=10000, default="N/A")
    location = models.CharField(max_length=1000, default="N/A")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Service Quote' 
        verbose_name_plural = 'Service Quote'


class ContactUs(models.Model):
    name = models.CharField(max_length=500, default="N/A")
    phone = models.CharField(max_length=500, default="N/A")
    email = models.CharField(max_length=500, default="N/A")
    message = models.CharField(max_length=10000, default="N/A")
    location = models.CharField(max_length=1000, default="N/A")
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Contact us' 
        verbose_name_plural = 'Contact us'


class Booking(models.Model):
    name = models.CharField(max_length=500)
    phone = models.CharField(max_length=500)
    email = models.CharField(max_length=500)
    message = models.CharField(max_length=10000)
    location = models.CharField(max_length=1000)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, blank=True, null=True)
    meeting_time = models.DateTimeField()
    duration_in_minutes = models.IntegerField(default=30)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = 'Booking' 
        verbose_name_plural = 'Booking'


class Email(models.Model):
    email = models.EmailField(unique=True, null=False)
    is_active = models.BooleanField(default=True)
    date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.email

    class Meta:
        verbose_name = 'Email Subscriber' 
        verbose_name_plural = 'Email Subscribers'
    


# django signal
def create_slug(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.name)

def create_slug_title(sender, instance, *args, **kwargs):
    instance.slug = slugify(instance.title)

def send_quote_email_signal(sender, instance, *args, **kwargs):
    send_email_quote(['emmanuelnwaegunwa@gmail.com', 'contact@bomachgroup.com'], instance)

def send_contact_email_signal(sender, instance, *args, **kwargs):
    send_email_contact(['emmanuelnwaegunwa@gmail.com', 'contact@bomachgroup.com'], instance)

def send_booking_email_signal(sender, instance, *args, **kwargs):
    send_booking_email(['emmanuelnwaegunwa@gmail.com', 'contact@bomachgroup.com'], instance)

def send_user_booking_email_signal(sender, instance, *args, **kwargs):
    send_user_booking_email(instance.email, instance)


pre_save.connect(create_slug, sender=Service)
pre_save.connect(create_slug, sender=SubService)
pre_save.connect(create_slug, sender=Project) # note this is proJEct
pre_save.connect(create_slug, sender=Product) # and this is proDUct
pre_save.connect(create_slug_title, sender=Blog)

post_save.connect(send_booking_email_signal, sender=Booking)
post_save.connect(send_user_booking_email_signal, sender=Booking)
post_save.connect(send_quote_email_signal, sender=Quote)
post_save.connect(send_contact_email_signal, sender=ContactUs)
