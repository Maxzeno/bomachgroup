from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse
from django.views import View
from django.conf import settings
from django.views.static import serve
from django.contrib import messages
# from django.http import Http404, HttpResponse
from .models import (
    Project as ProjectModel, Blog as BlogModel, Service as ServiceModel, 
    Employee, PartnerSlider, CustomerReview, HomeSlider, Quote as QuoteModel)

from .forms import QuoteForm

# Create your views here.

def serve_static(request, path):
    return serve(request, f'assets/{path}', document_root=settings.STATICFILES_DIRS[0])


class Base:
    context = {'services': ServiceModel.objects.all().order_by('-priority')}


class Index(View, Base):
    def get(self, request):
        projects = ProjectModel.objects.all().order_by('-priority')
        services3 = ServiceModel.objects.all().order_by('-priority')[:3]
        employees_count = Employee.objects.count()
        project_count = ProjectModel.objects.count()
        happy_customer = CustomerReview.objects.all().order_by('-priority')[:3]
        partners = PartnerSlider.objects.all().order_by('-priority')
        home_sliders = HomeSlider.objects.all().order_by('-priority')
        return render(request, 'main/index.html', {'projects': projects, 'services3': services3, 
            'employees_count': employees_count, 'project_count': project_count, 'home_sliders': home_sliders, 
            'happy_customer': happy_customer, 'partners': partners, **self.context})


class About(View, Base):
    def get(self, request):
        employees = Employee.objects.all().order_by('-priority')
        project_count = ProjectModel.objects.count()
        happy_customer_count = CustomerReview.objects.count()
        partners = PartnerSlider.objects.all().order_by('-priority')
        partners_3_grid = [[]]
        index = 0
        for i in range(len(partners)):
            if i % 3 == 0 and i != 0:
                index += 1
                partners_3_grid.append([])
            partners_3_grid[index].append(partners[i])
        print(partners_3_grid)
        return render(request, 'main/about.html', {'employees': employees, 'partners_3_grid': partners_3_grid, 
            'happy_customer_count': happy_customer_count, 'project_count': project_count, **self.context})


class Team(View, Base):
    def get(self, request):
        employees = Employee.objects.all().order_by('-priority')
        return render(request, 'main/team.html', {'employees': employees, **self.context})


class Blogs(View, Base):
    def get(self, request):
        blogs = BlogModel.objects.all().order_by('-priority')
        show_blog = blogs[:3]
        return render(request, 'main/blog.html', {'blogs': blogs, 'show_blog': show_blog, **self.context})


class Projects(View, Base):
    def get(self, request):
        services = ServiceModel.objects.all().order_by('-priority')
        projects = ProjectModel.objects.all().order_by('-priority')
        return render(request, 'main/project.html', {'projects': projects, **self.context})


class BlogDetail(View, Base):
    def get(self, request, pk):
        blog = get_object_or_404(BlogModel, pk=pk)
        blogs = BlogModel.objects.exclude(pk=blog.pk).order_by('-priority')
        return render(request, 'main/blog-details.html', {'blog': blog, 'blogs': blogs, **self.context})


class ProjectDetail(View, Base):
    def get(self, request, pk):
        project = get_object_or_404(ProjectModel, pk=pk)
        return render(request, 'main/project-details.html', {'project': project, **self.context})


class Service(View, Base):
    def get(self, request):
        services = ServiceModel.objects.all()
        return render(request, 'main/services.html', {**self.context})


class ServiceDetail(View, Base):
    def get(self, request):
        services = ServiceModel.objects.all()
        return render(request, 'main/service-details.html', {**self.context})


class Quote(View, Base):
    def get(self, request):
        form = QuoteForm()
        return render(request, 'main/free-estimate.html', {'form': form, **self.context})

    def post(self, request):
        form = QuoteForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, 'Message has been received')
            form = QuoteForm()
            return render(request, 'main/free-estimate.html', {"form": form, **self.context})

        messages.error(request, 'Invalid values fill try again', extra_tag='danger')
        return render(request, 'main/free-estimate.html', {"form": form, **self.context})
