from django.urls import path
from django.views.generic.base import TemplateView
from .import views

app_name = 'main'

urlpatterns = [
    path('', TemplateView.as_view(template_name='main/index.html'), name='home'),
    path('index', TemplateView.as_view(template_name='main/index.html'), name='index'),
    path('about', TemplateView.as_view(template_name='main/about.html'), name='about'),
    path('services', TemplateView.as_view(template_name='main/services.html'), name='services'),
    path('service-details', TemplateView.as_view(template_name='main/service-details.html'), name='service-details'),
    path('team', TemplateView.as_view(template_name='main/team.html'), name='team'),
    path('blog', TemplateView.as_view(template_name='main/blog.html'), name='blog'),
    path('project', TemplateView.as_view(template_name='main/project.html'), name='project'),
    path('blog-details', TemplateView.as_view(template_name='main/blog-details.html'), name='blog-details'),
    path('project-details', TemplateView.as_view(template_name='main/project-details.html'), name='project-details'),

    # path('blog/<slug:slug', BlogDetailView.as_view(template_name='main/blog-details.html'), name='blog-details'),
    # path('blog/<slug:slug', ProjectDetailView.as_view(template_name='main/project-details.html'), name='project-details'),


    path('assets/<path:path>', views.serve_static),

]
