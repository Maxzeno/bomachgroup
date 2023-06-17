from django.shortcuts import render, redirect
from django.urls import reverse
from django.views import View


# Create your views here.


class Index(View):
	def get(self, request, *args, **kwargs):
		return render(request, 'main/index.html', {})