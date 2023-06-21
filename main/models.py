from django.db import models
from django.utils import timezone
from django.utils.text import slugify
from django.db.models.signals import pre_save
from django.core.validators import MinValueValidator, MaxValueValidator
from ckeditor.fields import RichTextField

# Create your models here.


class ImageUrl:
    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/assets/img/logo/bomach-logo-full.jpeg'


class Service(models.Model, ImageUrl):
    name = models.CharField(max_length=500, unique=True)
    slug = models.CharField(max_length=500, blank=True)
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


class SubService(models.Model, ImageUrl):
    name = models.CharField(max_length=500, unique=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    slug = models.CharField(max_length=500, blank=True)
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


# django presave signal
def create_slug(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.name)

pre_save.connect(create_slug, sender=Service)


class Project(models.Model, ImageUrl):
    name = models.CharField(max_length=500, null=True, blank=True)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, null=True)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    min_budget = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    feedback = models.CharField(max_length=500, null=True, blank=True,)
    content = RichTextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class Blog(models.Model, ImageUrl):
    title = models.CharField(max_length=500, null=True, blank=True,)
    author = models.CharField(max_length=500, null=True, blank=True,)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class HomeSlider(models.Model, ImageUrl):
    # title = models.CharField(max_length=500)
    big_text = models.CharField(max_length=500)
    small_text = models.CharField(max_length=500)
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class CustomerReview(models.Model):
    name = models.CharField(max_length=500)
    review = models.CharField(max_length=2000)
    occupation = models.CharField(max_length=500)
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class Employee(models.Model, ImageUrl):
    name = models.CharField(max_length=500)
    job_title = models.CharField(max_length=500)
    facebook = models.CharField(max_length=200, null=True, blank=True)
    twitter = models.CharField(max_length=200, null=True, blank=True)
    instagram = models.CharField(max_length=200, null=True, blank=True)
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class PartnerSlider(models.Model, ImageUrl):
    company = models.CharField(max_length=500, default="N/A")
    image = models.ImageField(upload_to='images/')
    priority = models.IntegerField(default=0)
    date = models.DateTimeField(default=timezone.now)


class Quote(models.Model):
    name = models.CharField(max_length=500, default="N/A")
    phone = models.CharField(max_length=500, default="N/A")
    email = models.CharField(max_length=500, default="N/A")
    message = models.CharField(max_length=10000, default="N/A")
    location = models.CharField(max_length=1000, default="N/A")
    service = models.ForeignKey(Service, on_delete=models.CASCADE, null=True)
    sub_service = models.ForeignKey(SubService, on_delete=models.CASCADE, null=True)
    date = models.DateTimeField(default=timezone.now)

