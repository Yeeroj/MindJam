from django.shortcuts import render
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
# Create your views here.
def home(request):
    return render (request,'home.html')

def register(request):
    if request.method == 'POST':
        form=UserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request,'home.html')
    else:
        context={'form':UserCreationForm}
    return render (request,'signup.html', context)