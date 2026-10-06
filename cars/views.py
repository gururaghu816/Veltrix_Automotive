from django.shortcuts import render, redirect
from django.http import JsonResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from .models import Car
from .forms import TestDriveForm
from django.shortcuts import redirect

def home(request):
    if not request.user.is_authenticated:
        return redirect('login')
    cars = Car.objects.all()
    form = TestDriveForm()

    return render(request, 'index.html', {
        'cars': cars,
        'form': form
    })

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
    selected_car = Car.objects.filter(name__iexact="V8 Phantom").first()

    return render(request, "v8-phantom.html", {
        "v8_car": selected_car
    })

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


from django.shortcuts import render, redirect, get_object_or_404
from django.http import JsonResponse
from .models import TestDrive

def book_test_drive(request, car_id=None, featured_model=None):
    # If a car_id came from the URL, look it up. If it's invalid or missing,
    # selected_car stays None and the page falls back to the normal dropdown
    # behavior instead of throwing an error.
    selected_car = Car.objects.filter(id=car_id).first() if car_id else None

    if request.method == 'POST':
        form = TestDriveForm(request.POST)
        if featured_model:
            form.fields.pop('car', None)
        if selected_car:
            # The car dropdown isn't shown on this page, so it won't be in
            # the submitted data. Remove it from validation and set the
            # car manually instead.
            form.fields.pop('car', None)

        if form.is_valid():
            booking = form.save(commit=False)
            if featured_model:
                booking.featured_model = featured_model
            if selected_car:
                booking.car = selected_car
            booking.save()
            return render(request, 'success.html', {'booking': booking})
        else:
            print(form.errors)
    else:
        form = TestDriveForm()
        if featured_model or selected_car:
            form.fields.pop('car', None)

    return render(request, 'book_test_drive.html', {
        'form': form,
        'selected_car': selected_car,
    })


def save_signature(request, booking_id):
    if request.method == "POST":
        booking = get_object_or_404(TestDrive, id=booking_id)
        booking.signature = request.POST.get("signature", "")
        booking.signed = True
        booking.save()
        return JsonResponse({"status": "ok"})
    return JsonResponse({"status": "error"}, status=400)

def recommend_car(request):
    if request.method == "POST":
        budget = request.POST.get('budget')
        purpose = request.POST.get('purpose')
        fuel_type = request.POST.get('fuel_type')

        try:
            budget_val = float(budget)
        except (TypeError, ValueError):
            budget_val = None

        fallback_message = None
        cars = Car.objects.none()

        # Tier 1: exact match on budget, purpose, and fuel type
        if budget_val is not None:
            cars = Car.objects.filter(
                price__lte=budget_val,
                purpose__iexact=purpose,
                fuel_type__iexact=fuel_type
            )

        # Tier 2: drop fuel type, keep budget + purpose
        if not cars.exists() and budget_val is not None:
            relaxed = Car.objects.filter(
                price__lte=budget_val,
                purpose__iexact=purpose
            )
            if relaxed.exists():
                cars = relaxed
                fallback_message = (
                    f"No exact {fuel_type} match — showing other fuel types "
                    f"within your budget and purpose."
                )

        # Tier 3: drop purpose, keep budget + fuel type
        if not cars.exists() and budget_val is not None:
            relaxed = Car.objects.filter(
                price__lte=budget_val,
                fuel_type__iexact=fuel_type
            )
            if relaxed.exists():
                cars = relaxed
                fallback_message = (
                    f"No {purpose} cars found — showing other {fuel_type} "
                    f"options within your budget."
                )

        # Tier 4: ignore budget, keep purpose + fuel type (closest by price)
        if not cars.exists():
            relaxed = Car.objects.filter(
                purpose__iexact=purpose,
                fuel_type__iexact=fuel_type
            ).order_by('price')
            if relaxed.exists():
                cars = relaxed[:6]
                fallback_message = (
                    f"Nothing in your exact budget — here are the closest "
                    f"{purpose} {fuel_type} options we have."
                )

        # Tier 5: drop purpose and fuel type, keep budget only
        if not cars.exists() and budget_val is not None:
            relaxed = Car.objects.filter(price__lte=budget_val)
            if relaxed.exists():
                cars = relaxed
                fallback_message = (
                    "No cars matched your purpose and fuel type — "
                    "showing everything within your budget instead."
                )

        # Tier 6: absolute fallback — cheapest cars in the entire lineup
        if not cars.exists():
            cars = Car.objects.order_by('price')[:6]
            fallback_message = (
                "We couldn't find a close match — here are our most "
                "affordable models to start with."
            )

        return render(request, 'recommend_result.html', {
            'cars': cars,
            'fallback_message': fallback_message,
        })

    return render(request, 'recommend.html')