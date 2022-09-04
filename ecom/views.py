
from django.shortcuts import render

from .models import dest

# Create your views here.

def home(request):
    
    des = dest.objects.all() 

  
    return render(request,"myhtml.html",{"dest":des})
    
