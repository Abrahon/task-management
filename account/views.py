from django.shortcuts import render,redirect
from .forms import RegisterForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm,PasswordChangeForm,SetPasswordForm
from django.contrib.auth import authenticate,login,logout,update_session_auth_hash

# Create your views here.

def home(request):
    return render(request,'home.html')

def signup(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = RegisterForm(request.POST)
            if form.is_valid():
                
                form.save()
                print(form.cleaned_data)
                user = form.cleaned_data['username']
                password = form.cleaned_data['password1']
                messages.success(request, 'Account created successfully')
                user = authenticate(username=user, password=password)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
            
        else:
            form = RegisterForm()
        return render(request, './signup.html', {'form': form})
    else:
        return redirect('profile')


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user = form.cleaned_data['username']
                userpass = form.cleaned_data['password']
                user = authenticate(username=user, password=userpass)
                if user is not None:
                    login(request, user)
                    return redirect('profile')
        else:
            form=AuthenticationForm()   
        return render(request, 'login.html',{'form': form})
    else:
        
        return redirect('profile')

def profile(request):
    if request.user.is_authenticated:
        return render(request,'profile.html',{'user': request.user})
    else:
        return redirect('login')


def user_logout(request):
    logout(request)
    return redirect('login')

def pass_change(request):
    if request.method == 'POST':
        form = PasswordChangeForm(request.user, request.POST)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request.user)
            return redirect('profile')
        # else:
            # messages.success(request, 'Your password was successfully updated!')
            # return redirect('change_password')
    else:
        form = PasswordChangeForm(request.user)
        
    return render(request, 'pass_change.html', {'form': form})
    
    
