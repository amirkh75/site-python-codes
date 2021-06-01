
from django.shortcuts import render,redirect
from django.contrib.auth import get_user_model
from django.contrib import auth
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required


def users_detail(request, user_id):
    User = get_user_model()
    user = get_object_or_404(User, id = user_id)

    return render(request,'users/users_detail.html', {'user': user})

def signup(request):
    User = get_user_model()
    if request.method == "POST":
        if request.POST['password1'] == request.POST['password2']:
            try:
                User.objects.get(email = request.POST['email'])
                return render (request,'users/signup.html', {'error':'email is already for a user!'})
            except User.DoesNotExist:
                user = User.objects.create_user(request.POST['email'],password=request.POST['password1'])
                auth.login(request,user)
                return redirect('home')
        else:
            return render (request,'users/signup.html', {'error':'Password does not match!'})
    else:
        return render(request,'users/signup.html')

def login(request):
    if request.method == 'POST':
        user = auth.authenticate(email=request.POST['email'],password = request.POST['password'])
        if user is not None:
            auth.login(request,user)
            return redirect('home')
        else:
            return render (request,'users/login.html', {'error':'Username or password is incorrect!'})
    else:
        return render(request,'users/login.html')

def logout(request):
    if request.method == 'POST':
        auth.logout(request)
        return redirect('home')
    
    else:
        return render(request, 'users/logout.html')

