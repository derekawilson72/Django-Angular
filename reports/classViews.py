from django.http import HttpResponse
from django.views.generic import View, TemplateView
from django.shortcuts import render


class MyView(View):

    def get(self, request, *args, **kwargs):
        return HttpResponse('Hello, World!')



class AboutView(TemplateView):
    template_name = "about.html"
    def get(self, request, *args, **kwargs):
        return request
