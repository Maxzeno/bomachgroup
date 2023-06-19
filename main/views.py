from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.views.static import serve
# from django.http import Http404, HttpResponse
from .models import Project as ProjectModel, Blog as BlogModel

# Create your views here.

def serve_static(request, path):
    return serve(request, f'assets/{path}', document_root=settings.STATICFILES_DIRS[0])


class Index(View):
    def get(self, request):
        projects = ProjectModel.objects.all()
        return render(request, 'main/index.html', {'projects': projects})


class Blogs(View):
    def get(self, request):
        blogs = BlogModel.objects.all()
        show_blog = blogs[:3]
        return render(request, 'main/blog.html', {'blogs': blogs, 'show_blog': show_blog})


class Projects(View):
    def get(self, request):
        projects = ProjectModel.objects.all()
        return render(request, 'main/project.html', {'projects': projects})


class BlogDetail(View):
    def get(self, request, pk):
        blog = get_object_or_404(BlogModel, pk=pk)
        blogs = BlogModel.objects.exclude(pk=blog.pk)
        return render(request, 'main/blog-details.html', {'blog': blog, 'blogs': blogs})


class ProjectDetail(View):
    def get(self, request, pk):
        project = get_object_or_404(ProjectModel, pk=pk)
        return render(request, 'main/project-details.html', {'project': project})

