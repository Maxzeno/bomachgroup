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
    path('blog', TemplateView.as_view(template_name='main/blog.html'), name='blog'),
    path('blog-details', TemplateView.as_view(template_name='main/blog-details.html'), name='blog-details'),
    path('contact', TemplateView.as_view(template_name='main/contact.html'), name='contact'),
    path('project', TemplateView.as_view(template_name='main/project.html'), name='project'),
    path('project-details', TemplateView.as_view(template_name='main/project-details.html'), name='project-details'),
    path('team', TemplateView.as_view(template_name='main/team.html'), name='team'),
    path('team-details', TemplateView.as_view(template_name='main/team-details.html'), name='team-details'),

    path('index.html', TemplateView.as_view(template_name='main/index.html'), name='index'),
    path('about.html', TemplateView.as_view(template_name='main/about.html'), name='about'),
    path('services.html', TemplateView.as_view(template_name='main/services.html'), name='services'),
    path('service-details.html', TemplateView.as_view(template_name='main/service-details.html'), name='service-details'),
    path('blog.html', TemplateView.as_view(template_name='main/blog.html'), name='blog'),
    path('blog-details.html', TemplateView.as_view(template_name='main/blog-details.html'), name='blog-details'),
    path('contact.html', TemplateView.as_view(template_name='main/contact.html'), name='contact'),
    path('project.html', TemplateView.as_view(template_name='main/project.html'), name='project'),
    path('project-details.html', TemplateView.as_view(template_name='main/project-details.html'), name='project-details'),
    path('team.html', TemplateView.as_view(template_name='main/team.html'), name='team'),
    path('team-details.html', TemplateView.as_view(template_name='main/team-details.html'), name='team-details'),


    path('<path:path>', views.serve_static),

]
