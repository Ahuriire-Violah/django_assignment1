from django.shortcuts import render 
from django.http import HttpResponse

# Create your views here.
from django.http import HttpResponse
def home(request):
    return HttpResponse("Ahuriire Violah")


def homepage(request):
    return HttpResponse("Hi World,  This is Viola")

def contact(request):
    return HttpResponse("Contact us on the following numbers 0707419671 ")

from django.shortcuts import render
def login(request):
    return render(request,'login.html')