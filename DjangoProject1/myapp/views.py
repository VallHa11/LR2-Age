from django.shortcuts import render
from django.http import HttpResponse

def door_detail(request, door_id):
    return render(request, 'myapp/door_detail.html', {'door_id': door_id})

def search_doors(request, query):

    return render(request, 'myapp/search_results.html', {'query': query})

def index(request):
    return render(request, 'myapp/index.html')

def contact(request):
    return render(request, 'myapp/contact.html')

def doors(request):
    return render(request, 'myapp/doors.html')