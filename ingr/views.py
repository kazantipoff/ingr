from django.shortcuts import render
from events.models import Events


def index(request):
    return render(request, 'index.html')


def weapon(request):
    return render(request, 'weapon.html')


def history(request):
    return render(request, 'history.html')


def contacts(request):
    return render(request, 'contacts.html')


def events(request):
    events = Events.objects.all()
    return render(request, 'event.html', {'events': events})
