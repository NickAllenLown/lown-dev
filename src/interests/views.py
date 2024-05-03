from django.shortcuts import render
from django.http.response import HttpResponse
from django.urls import reverse
# Create your views here.

def interest_view(request):
    return render(request,'interests/interests.html')
