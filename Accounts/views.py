
from django.contrib.auth.models import Group
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from student_portal.models import Request
from django.shortcuts import render

# Create your views here.
from django.shortcuts import render, redirect


def main_page(request):
    return render(request, 'home/index2.html')

def login_view(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)

            if user.groups.filter(name='mentor').exists():
                return redirect('mentor_home')

            elif user.groups.filter(name='faculty').exists():
                return redirect('faculty')

            elif user.groups.filter(name='hostel').exists():
                return redirect('supervisor_home')

            elif user.groups.filter(name='students').exists():
                return redirect('stud_home')

            elif user.groups.filter(name='warden').exists():
                return redirect('warden_home')
        else:
            error_message = 'Invalid ID or password'
            return render(request, 'home/Login1.html', {'error_message': error_message})

    # Return the login page template for GET requests
    return render(request, 'home/Login1.html')


def register(request):
    if request.method == 'POST':
        # Get user input data from the form
        username = request.POST['username']
        email = request.POST['email']
        password1 = request.POST['password1']
        password2 = request.POST['password2']

        # Check if passwords match
        if password1 != password2:
            messages.error(request, "Passwords do not match")
            return redirect('register')

        # Check if user with same username or email already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, "Username already exists")
            return redirect('register')
        if User.objects.filter(email=email).exists():
            messages.error(request, "Email already exists")
            return redirect('register')

        # Create user
        user = User.objects.create_user(
            username=username, email=email, password=password1)

        # Add user to group
        group = Group.objects.get(name='students')
        user.groups.add(group)

        user.save()
        messages.success(request, "Account created successfully")
        return redirect('login')
    else:
        return render(request, 'home/reg.html')


def LogoutUser(request):
    logout(request)
    return redirect('login')
