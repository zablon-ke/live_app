from django.shortcuts import render

# Create your views here.
def index(request):
    
    name="Alex"
    
    
    return render(request,"live/base.html",{"name":name})