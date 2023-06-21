from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Group
from ckeditor.widgets import CKEditorWidget
from .models import Project, Blog, Service, SubService, HomeSlider, CustomerReview, Employee, PartnerSlider, Quote

# Register your models here.

admin.site.site_title = 'Bomach Group Admin'
admin.site.index_title = 'Welcome to Bomach Group'
admin.site.site_header = format_html('<a href="/admin/"><img src="/static/assets/img/logo/bomach-logo-full.jpeg" style="height: 100px"></a>')

admin.site.unregister(Group)


@admin.register(Service)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'image', 'content', 'rating', 'priority', 'date')
    list_display = ('name', 'slug', 'rating', 'priority', 'date')
    search_fields = ('name','slug')
    formfield_overrides = {
        'RichTextField': {'widget': CKEditorWidget}
    }


@admin.register(SubService)
class ServiceAdmin(admin.ModelAdmin):
    fields = ('name', 'service', 'slug', 'image', 'content', 'rating', 'priority', 'date')
    list_display = ('name', 'slug', 'rating', 'priority', 'date')
    search_fields = ('name','slug')
    formfield_overrides = {
        'RichTextField': {'widget': CKEditorWidget}
    }



@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'slug', 'sub_service', 'feedback', 'image', 'min_budget', 'max_budget', 'content', 'priority', 'date')
    list_display = ('name', 'slug', 'feedback', 'min_budget', 'max_budget', 'priority', 'date')
    search_fields = ('name',)
    formfield_overrides = {
        'RichTextField': {'widget': CKEditorWidget}
    }


@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'slug', 'author', 'image', 'content', 'priority', 'date')
    list_display = ('title', 'slug', 'author', 'priority', 'date')
    search_fields = ('title', 'author')
    formfield_overrides = {
        'RichTextField': {'widget': CKEditorWidget}
    }


@admin.register(HomeSlider)
class HomeSliderAdmin(admin.ModelAdmin):
    fields = ('big_text', 'small_text', 'image', 'priority', 'date')
    list_display = ('big_text', 'small_text', 'priority', 'date')
    search_fields = ('big_text',)


@admin.register(CustomerReview)
class CustomerReviewAdmin(admin.ModelAdmin):
    fields = ('name', 'review', 'occupation', 'priority', 'date')
    list_display = ('name', 'review', 'occupation', 'priority', 'date')
    search_fields = ('name', 'occupation')


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    fields = ('name', 'job_title', 'facebook', 'twitter', 'instagram', 'image', 'priority', 'date')
    list_display = ('name', 'job_title', 'facebook', 'twitter', 'instagram', 'priority', 'date')
    search_fields = ('name', 'job_title')


@admin.register(PartnerSlider)
class PartnerSliderAdmin(admin.ModelAdmin):
    fields = ('company', 'image', 'priority', 'date')
    list_display = ('company', 'priority', 'date')
    search_fields = ('company',)


@admin.register(Quote)
class QuoteAdmin(admin.ModelAdmin):
    fields = ('name', 'phone', 'email', 'location', 'message', 'service', 'sub_service', 'date')
    list_display = ('name', 'phone', 'email', 'location', 'message', 'date')
    search_fields = ('name',)

