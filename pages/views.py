from django.shortcuts import render

# Create your views here.
def home(request):
    return render(request, 'home.html', {})


def about(request):
    from pages.namer import name
    return render(request, 'about.html', {"name": name()})

def contact(request):
    return render(request, 'contact.html', {})