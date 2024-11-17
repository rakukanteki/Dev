from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.models import User, auth
from django.contrib import messages
from .models import Feature

# Create your views here.
def index(request):
    feature1 = Feature()
    feature1.id = 2010020
    feature1.name = 'Radwan'
    feature1.details = 'Studies in dept. of Electrical and Computer Engineering'
    feature1.is_true = True

    feature2 = Feature()
    feature2.id = 2010033
    feature2.name = 'Galib'
    feature2.details = 'Studies in dept. of Electrical and Communication Engineering'
    feature2.is_true = False

    feature3 = Feature()
    feature3.id = 2010049
    feature3.name = 'Dudun'
    feature3.details = 'Studies in dept. of Electrical and Computer Engineering'
    feature3.is_true = True

    feature4 = Feature()
    feature4.id = 2010053
    feature4.name = 'Rejuan'
    feature4.details = 'Studies in dept. of Electrical and Computer Engineering'
    feature4.is_true = True

    features = [feature1, feature2, feature3, feature4]

    return render(request, 'index.html', {'features': features})

def blogs(request):
    features = Feature.objects.all()
    return render(request, 'blog.html', {'features': features})

def registration(request):
    if request.method == "POST":
    # text = request.GET.get('text', '') # For GET methods
        text = request.POST.get('text', '')
        amount_words = len(text.split())
        return render(request, 'registration.html', {'total_words': amount_words})
    else:
        return render(request, 'registration.html')

# def counter(request):
#     text = request.GET['text']
#     amount_words = len(text.split())
#     return render(request, 'counter.html', {'total_words': amount_words})

def about(request):
    context = {
        'name': 'Radwan',
        'age': 23,
        'nationality': 'Bangladeshi',
    }
    return render(request, 'about.html', context)

def radwan(request):
    name = 'Radwan'
    return render(request, 'radwan.html', {'name': name})

def register(request):
    # Collecting data from the frontend.
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        password2 = request.POST.get('password2')

        if password == password2: # Check if the passwords are correct.
            if User.objects.filter(email=email).exists(): # Check if the email already exists.
                messages.info(request, "Email already used. Try another email")
                return redirect('register') # If email already exists, redirect to register process.
            elif User.objects.filter(username=username).exists(): # Check if username already exists.
                messages.info(request, "Username already exists")
                return redirect('register')
            else: # If all above passes, create a new user.
                user = User.objects.create_user(username=username, email=email, password=password)
                user.save()
                return redirect('login')
        else: # Check if password doesn't match.
            messages.info(request, 'Password are not same.')
            return redirect('register')
    else: # If the method is not POST.
        return render(request, 'register.html')

def login(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Credentials Invalid')
            return redirect('login')
    else:
        return render(request, 'login.html')

def logout(request):
    auth.logout(request)
    return redirect('/')