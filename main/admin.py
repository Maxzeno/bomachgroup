from django.contrib import admin
from django.utils.html import format_html
from django.contrib.auth.models import Group
from ckeditor.widgets import CKEditorWidget
from .models import Project, Blog

# Register your models here.

admin.site.site_title = 'Bomach Group Admin'
admin.site.index_title = 'Welcome to Bomach Group'
admin.site.site_header = format_html('<a href="/admin/"><img src="/static/assets/img/logo/bomach-logo-full.jpeg" style="height: 100px"></a>')

admin.site.unregister(Group)

@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    fields = ('name', 'service', 'feedback', 'image', 'min_budget', 'max_budget', 'content', 'date')
    list_display = ('name', 'service', 'feedback', 'date')
    search_fields = ('name','service')
    formfield_overrides = {
        'RichTextField': {'widget': CKEditorWidget}
    }

    # class Media:
    #     css = {
    #         'all': ('django-admin-custom.css', ),
    #     }

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    fields = ('title', 'author', 'image', 'content', 'date')
    list_display = ('title', 'author', 'date')
    search_fields = ('title', 'author')
    formfield_overrides = {
        'RichTextField': {'widget': CKEditorWidget}
    }

    # class Media:
    #     css = {
    #         'all': ('django-admin-custom.css', ),
    #     }
