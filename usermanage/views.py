from django.contrib.auth.decorators import login_required
from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.shortcuts import render, redirect
from usermanage.forms import LoginForm, SignupForm
from django.contrib.auth.models import User


def index(request):
    return render(request, 'usermanage/index.html')

@login_required
def dashboard(request):
    return render(request, 'usermanage/dashboard.html')


def signup_custom(request):
    if request.method == 'POST':
        form = SignupForm(request.POST)
        if form.is_valid():
            first_name = request.POST['first_name']
            last_name = request.POST['last_name']
            username = request.POST['username']
            password = request.POST['password']
            email = request.POST['email']

            #TO DO CHECK IF IT ALREADY EXISTS

            user = User.objects.create_user(username=username, password=password, email=email)
            user.save()

            login(request, user)
            return redirect('dashboard')
    else:
        form = SignupForm()
        return render(request, 'registration/signup.html', {'form': form})


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