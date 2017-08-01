from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from usermanage.models import Restaurant, Customer
from django.shortcuts import render, redirect
from usermanage.forms import LoginForm, SignupForm
from django.contrib.auth.models import User
from django.core.exceptions import ObjectDoesNotExist


def index(request):
    return render(request, 'usermanage/index.html')

@login_required
def dashboard(request):
    user = request.user
    try:
        user.restaurant
        return render(request, 'usermanage/dashboard_restaurant.html')
    except:
        return render(request, 'usermanage/dashboard.html')


def signup_customer(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            #TO DO CHECK IF IT ALREADY EXISTS

            user1 = User.objects.create_user(username=username, password=password,email=email)
            user1.save()
            user = Customer(customer_user=user1)
            user.save()

            login(request, user1)
            return redirect('dashboard')
    else:
        form = SignupForm()
        return render(request, 'registration/signup_customer.html', {'form': form})


def signup_restaurant(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            #TO DO CHECK IF IT ALREADY EXISTS

            user1 = User.objects.create(username=username, password=password,
                                            email=email, first_name = first_name,
                                            last_name = last_name)
            user1.save()
            user = Restaurant.objects.create(restaurant_user = user1)
            user.save()

            login(request, user1)
            return redirect('dashboard')
    else:
        form = SignupForm()
        return render(request, 'registration/signup_restaurant.html', {'form': form})


def login_custom(request):
    if request.method == 'POST':
        form = LoginForm(request.POST)
        if form.is_valid():
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            context = {user:user}
            if user is not None:
                login(request, user)
                return render(request, 'usermanage/dashboard.html', context)
    else:
        form = LoginForm
        return render(request, 'registration/login.html',{'form':form})


@login_required
def logout_custom(request):
    if request.method == 'POST':
        logout(request)
        return render(request, 'usermanage/index.html')
    else:
        return render(request, 'registration/logout.html')


def dashboard_restaurant(request):
    return render(request, 'usermanage/dashboard_restaurant.html')