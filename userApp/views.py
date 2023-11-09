from django.shortcuts import render
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import login, authenticate, logout
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.contrib.auth.decorators import login_required
from .forms import SignUpForm, UserProfileChange

# Create your views here.
def sign_up(request):
    form = SignUpForm()
    registered = False
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            registered = True
    dict = {'title':'Create Account', 'form': form, 'registered':registered,}
    return render(request, 'userApp/signup.html', context=dict)

def sign_in(request):
    form = AuthenticationForm()
    if request.method == 'POST':
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            if user is not None:
                login(request, user)
                return HttpResponseRedirect(reverse('userApp:dashboard'))    
    dict = {'title':'Sign in your account', 'form':form}
    return render(request, 'userApp/signin.html', context = dict)

@login_required
def logout_user(request):
    logout(request)
    return HttpResponseRedirect(reverse('homeApp:home'))

@login_required
def edit_profile(request):
    current_user = request.user
    form = UserProfileChange(instance=current_user)
    if request.method == 'POST':
        form = UserProfileChange(request.POST, instance=current_user)
        if form.is_valid():
            form.save()
            form = UserProfileChange(instance=current_user)
    dict = {'title':'Edit Profile', 'form': form,}
    return render(request, 'userApp/editProfile.html', context=dict)

@login_required
def author_profile(request, username):
    dict = {'title':'Author Profile',}
    return render(request, 'userApp/authorProfile.html', context=dict)


def dashboard(request):
    dict = {'title': 'Dashboard',}
    return render(request, 'userApp/dashboard.html', context= dict)


