from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User , auth

def home(request):
    return render(request, 'index.html')
def about(request):
    return render(request, 'about.html')
def signup(request):
    #return render(request, 'signup.html')
def dashboard(request):
    return render(request, 'dashboard.html')
def login(request):
    return render(request, 'login.html')
    
    
def signup(request):
    if request.method == 'POST':
        name = request.POST['name'],
        email = request.POST['email'],
        password = request.POST['password'],
        cnf_password = request.POST['cnf_password'],
        
        if password == cnf_password:
            user = User.objects.create_user(name=name, email= email , password=password)
            User.save();
            print('user created')
            return redirect('signup.html')
    return render(request,'signup.html')
