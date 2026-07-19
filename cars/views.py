from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Car
from .forms import TestDriveForm


def home(request):
    return render(request, "index.html")

def models_page(request):
    return render(request, "models.html")

def compare_page(request):
    return render(request, "compare.html")

def about_page(request):
    return render(request, "about.html")

def contact_page(request):
    return render(request, "contact.html")


def get_cars(request):
    cars = list(Car.objects.values())
    return JsonResponse(cars, safe=False)


def v8_phantom(request):
    return render(request, "v8-phantom.html")

def x9_dominator(request):
    return render(request, "x9-dominator.html")

def hyundai_verna(request):
    return render(request, "hyundai-verna.html")
def land_rover_defender(request):
    return render(request, "land_rover_defender.html")



def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, "Invalid Username or Password")

    return render(request, "login.html")


def logout_view(request):
    logout(request)
    return redirect('/login/')


def book_test_drive(request):
    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
        else:
            print(form.errors)  
    else:
        form = TestDriveForm()

    return render(request, 'book_test_drive.html', {'form': form})

def recommend_car(request):

    if request.method == "POST":

        budget = request.POST.get('budget')
        purpose = request.POST.get('purpose')
        fuel_type = request.POST.get('fuel_type')

        cars = Car.objects.filter(
            price__lte=budget,
            purpose=purpose,
            fuel_type=fuel_type
        )

        return render(
            request,
            'recommend_result.html',
            {'cars': cars}
        )

    return render(
        request,
        'recommend.html'
    )