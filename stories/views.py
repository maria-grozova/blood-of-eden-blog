from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def stories(request):
    return HttpResponse('Stories go here')