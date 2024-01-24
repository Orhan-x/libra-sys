from django.shortcuts import render
from .forms import RegisterForm, LoginForm
from django.http import HttpResponse

def registeration(request):
    
    context = {}
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        
        if form.is_valid():
            form.save()
            # to add flashing message
    else: 
        form = RegisterForm()
        
    context['form'] = form
        
    return render(request, 'authentication/signup.html', context)
    
    
    
def login(request):
    context = {}
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            pass
            #business login here 
            # return HttpResponse(f"cni: {request.POST.get('cni')}\n pass: {request.POST.get('password')}")
            # to add flashing message
            # to add flashing message
    else: 
        form = LoginForm()
        
    context['form'] = form
        
    return render(request, 'authentication/signup.html', context)