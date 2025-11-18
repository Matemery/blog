from django.shortcuts import render
from django.views.generic import TemplateView
# Create your views here.
class HomePageView(TemplateView): # Class based view
    template_name = "pages/home.html" # link our view to the html

class AboutPageView(TemplateView):
    template_name = "pages/about.html"