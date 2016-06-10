from django.shortcuts import render
from django.views.generic import TemplateView,View


class Home(TemplateView):
	template_name="rock/home.html"


class Callback(TemplateView):
	template_name="rock/callback.html"
