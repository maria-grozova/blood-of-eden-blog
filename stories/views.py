from django.shortcuts import render
from django.views import generic
from .models import Story

# Create your views here.
class StoriesList(generic.ListView):
    queryset = Story.objects.all()
    template_name = "stories/index.html"
    paginate_by = 3