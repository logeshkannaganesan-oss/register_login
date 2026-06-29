from django.shortcuts import render, redirect
from .forms import RegisterForm
from .models import UserRegister

def register(request):
    if request.method == "POST":
        form = RegisterForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('login')
    else:
        form = RegisterForm()
    return render(request, 'register.html', {'form': form})

def login_view(request):
    error = None
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            user = UserRegister.objects.get(username=username, password=password)
            request.session['username'] = user.username
            return redirect('home')
        except UserRegister.DoesNotExist:
            error = 'Invalid Username or Password configuration.'

    return render(request, 'login.html', {'error': error})

def home(request):
    username = request.session.get('username')
    if not username:
        return redirect('login')
    return render(request, 'home.html', {'username': username})

def logout_view(request):
    request.session.flush() # Completely wipes the session database entry
    return redirect('login')