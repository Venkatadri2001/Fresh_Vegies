from django.shortcuts import render
from django.http import HttpResponse
from .models import Vegetables




def index(request):
    vegetables = Vegetables.objects.all()
    return render(request, 'index.html', {'vegetables': vegetables})
