from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required


# Create your views here.
def base_html(request):
    return render(request, 'base.html')


def aboutus(request):
    return render(request, 'aboutus.html')

@login_required(login_url="/login/")
def recipies(request):
    if request.method == "POST":
        data = request.POST
        recipie_name = data.get('recipie_name')
        recipie_description = data.get('recipie_description')
        recipie_image = request.FILES.get('recipie_image')

        Recipie.objects.create(
            recipie_name = recipie_name,
            recipie_description = recipie_description,
            recipie_image = recipie_image,
        )

        return redirect('/view_recipies/')
    
    return render(request, 'recipies.html')

@login_required(login_url="/login/")
def view_recipies(request):
    queryset = Recipie.objects.all()

    if request.GET.get('search'):
        queryset = queryset.filter(recipie_name__icontains = request.GET.get('search'))

        print(request.GET.get('search'))

    context = {'recipies': queryset}
    return render(request, 'view_recipies.html', context)


@login_required(login_url="/login/")
def delete_recipie(request, id):
    queryset = Recipie.objects.get(id = id)
    queryset.delete()
    return redirect('/view_recipies/')


@login_required(login_url="/login/")
def update_recipie(request, id):
    queryset = Recipie.objects.get(id = id)
    if request.method == "POST":
        data = request.POST
        recipie_name = data.get('recipie_name')
        recipie_description = data.get('recipie_description')
        recipie_image = request.FILES.get('recipie_image')

        queryset.recipie_name = recipie_name
        queryset.recipie_description = recipie_description

        if recipie_image:
            queryset.recipie_image = recipie_image

        queryset.save()
        return redirect('/view_recipies/')

    context = {'recipie': queryset}
    return render(request, 'update_recipies.html', context)
    

def login_page(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        print(password)

        if not User.objects.filter(username = username).exists():
            messages.info(request, "Invalid Username.")
            return redirect('/login/')
        
        user = authenticate(username = username, password = password)

        if user is None:
            messages.info(request, "Invalid Username or Password.")
            return redirect('/login/')
        else:
            login(request, user)
            return redirect('/recipies/')

    return render(request, 'login.html')


def logout_page(request):
    logout(request)
    return redirect('/login/')


def register(request):
    if request.method == 'POST':
        first_name = request.POST.get('first_name')
        last_name = request.POST.get('last_name')
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = User.objects.filter(username = username)

        if user.exists():
            messages.info(request, "Username already taken.")
            return redirect('/register/')

        user = User.objects.create(
            first_name = first_name,
            last_name = last_name,            
            username = username,
        )
        user.set_password(password)
        user.save()
        print(f"{first_name}, {last_name}, {username}, {password}")
        messages.info(request, "Account created successfully.")


        return redirect('/register/')

    return render(request, 'register.html')


@login_required(login_url='/login/')
def profile(request):
    return render(request, 'profile.html')


@login_required(login_url='/login/')
def edit_profile(request):
   if request.method == 'POST':
        user_id = request.user.id
        user = User.objects.get(id=user_id)

        user.first_name = request.POST.get('first_name')
        user.last_name = request.POST.get('last_name')
        user.username = request.POST.get('username')

        user.save()
        return redirect('/profile/')

   return render(request, 'edit_profile.html')