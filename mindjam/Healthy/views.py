from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Profile
# Create your views here.
def home(request):
    return render (request,'home.html')

def add(request):
    if request.method == 'POST':
        area=request.POST["area"]
        malaria=request.POST["malaria"]
        dengue=request.POST["dengue"]
        aids=request.POST["aids"]
        cancer=request.POST["cancer"]
        corona=request.POST["corona"]
        polio=request.POST["polio"]
        profile=Profile(Area = area,Malaria=malaria, Dengue=dengue, Aids=aids, Cancer=cancer, Corona=corona, Polio=polio)
        profile.save();
        return render(request,'home.html')
    else:



        return  render(request,'add.html')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        context={'form':UserCreationForm}
    return render (request,'signup.html', context)