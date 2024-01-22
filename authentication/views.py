from django.shortcuts import render
from .forms import RegisterForm

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
    return render(request, 'authentication/login.html', {})

