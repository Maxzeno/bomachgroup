from django.urls import path
from django.views.generic.base import TemplateView
from .import views

app_name = 'main'

urlpatterns = [
    path('', views.Index.as_view(), name='home'),
    path('index', views.Index.as_view(), name='index'),
    path('about', views.About.as_view(), name='about'),
    path('services', views.Service.as_view(), name='services'),
    path('service-details', views.ServiceDetail.as_view(), name='service-details'),
    path('get-sub-service', views.GetSubService.as_view(), name='get-sub-service'),
    path('team', views.Team.as_view(), name='team'),
    path('blog', views.Blogs.as_view(), name='blog'),
    path('project', views.Projects.as_view(), name='project'),
    path('blog/<int:pk>', views.BlogDetail.as_view(), name='blog-details'),
    path('project/<int:pk>', views.ProjectDetail.as_view(), name='project-details'),

    # might be removed 
    # path('free-estimate', views.Quote.as_view(), name='free-estimate'),
    
    path('assets/<path:path>', views.serve_static),
]
