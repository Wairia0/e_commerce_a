from django.shortcuts import render


def home(request):
    context = {
        
        "page_title": "Home Page",
        "user_name": "Wairia",
    }
    return render(request, "home.html")

def about(request):
    return render(request, "about.html")


def dashboard(request):
    context = {
        "user_name": "Kamau",
        "is_admin": True
    }
    return render(request, "dashboard.html")

def shoppinglist(request):
    context = {
        "shoppinglist": ["Milk", "Eggs", "Butter"]
    }
    return render(request, "shoppinglist.html", context)