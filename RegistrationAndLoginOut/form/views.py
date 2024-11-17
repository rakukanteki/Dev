from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages

# Create your views here.
def registerlogin(request):
    return render(request, 'registerlogin.html')

def login(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = auth.authenticate(username=username, password=password)
        if user is not None: # If the user is registerd. Go to homepage.
            auth.login(request, user)
            return redirect('home')
        else: # If the user is not registered.
            messages.error(request, 'Invalid credentials, please try again.')
            return redirect('login')
    else:
        return render(request, 'login.html')

def register(request):
    if request.method == 'POST':
        # Fetching information from frontend.
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        # Checking password and password2 are same.
        if password == password2:
            if User.objects.filter(email=email).exists(): # Check if already email exists
                messages.error(request, "Email is already taken.")
                return redirect('register')
            elif User.objects.filter(username=username).exists(): # Check if username already exists.
                messages.info(request, 'Username already exists. Try another one.')
                return redirect('register')
            else: # If all the cases passed, create a new user.
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                messages.success(request, "Registration successful! Please log in.")
                return redirect('login')
        else: # If password doesn't match.
            messages.info(request, 'Passwords did not match. Try again.')
            return redirect('register')
    else: # If the method is not POST.
        return render(request, 'register.html')
    

def logout(request):
    auth.logout(request)
    return redirect('registerlogin')

def home(request):
    return render(request, 'home.html')