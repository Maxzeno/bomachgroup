from django.db import models
from django.utils import timezone
from ckeditor.fields import RichTextField

# Create your models here.

class Project(models.Model):
    TAG_CHOICES = (
        ('REAL-ESTATE-SERVICES', 'REAL ESTATE SERVICES'),
        ('LAND-SERVICES', 'LAND SERVICES'),
        ('ENGINEERING-CONSTRUCTION', 'ENGINEERING / CONSTRUCTION'),
        ('WEB-DEVELOPMENT-BUSINESS-AUTOMATION', 'WEB DEVELOPMENT / BUSINESS AUTOMATION'),
        ('LOGISTICS-SERVICES', 'LOGISTICS SERVICES'),
        ('FOOD-AND-FARM', 'FOOD AND FARM'),
    )
    
    tag = models.CharField(max_length=255, choices=TAG_CHOICES)
    name = models.CharField(max_length=500, null=True, blank=True,)
    service = models.CharField(max_length=500, null=True, blank=True,)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    min_budget = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    max_budget = models.DecimalField(max_digits=20, decimal_places=4, blank=True, null=True)
    feedback = models.CharField(max_length=500, null=True, blank=True,)
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/assets/img/logo/bomach-logo-full.jpeg'


class Blog(models.Model):
    title = models.CharField(max_length=500, null=True, blank=True,)
    author = models.CharField(max_length=500, null=True, blank=True,)
    image = models.ImageField(upload_to='images/', blank=True, null=True)
    content = RichTextField(blank=True, null=True)
    date = models.DateTimeField(default=timezone.now)

    def image_url(self):
        if self.image:
            return self.image.url
        return '/static/assets/img/logo/bomach-logo-full.jpeg'
