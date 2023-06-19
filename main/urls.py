from django.urls import path
from django.views.generic.base import TemplateView
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('index', views.Index.as_view(), name='index'),
    path('about', TemplateView.as_view(template_name='main/about.html'), name='about'),
    path('services', TemplateView.as_view(template_name='main/services.html'), name='services'),
    path('service-details', TemplateView.as_view(template_name='main/service-details.html'), name='service-details'),
    path('team', TemplateView.as_view(template_name='main/team.html'), name='team'),
    
    path('blog', views.Blogs.as_view(), name='blog'),
    path('project', views.Projects.as_view(), name='project'),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blog-details'),
    path('project/<int:pk>', views.ProjectDetail.as_view(), name='project-details'),

    path('assets/<path:path>', views.serve_static),
]
