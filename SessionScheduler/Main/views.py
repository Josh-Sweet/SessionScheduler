from django.shortcuts import render, get_object_or_404, redirect
from django.forms import modelform_factory

# Create your views here.
from DataModels.models import Session, Attendant, Location


# Renders the main welcome page
def welcome(request):
    return render(request, "Main/WelcomePage.html",
                  {"numAttendants": Attendant.objects.count(),
                   "numSessions": Session.objects.count(),
                   "sessionList": Session.objects.all()})


# Renders the page detailing the session information
def session_detail(request, id):
    session = get_object_or_404(Session, pk=id)
    return render(request, "Main/SessionDetail.html", {"Session": session})


# Renders the page showing the list of locations
def locations(request):
    return render(request, "Main/Locations.html", {"locationList": Location.objects.all()})


# The form model for session data.
SessionForm = modelform_factory(Session, exclude=[])


# Renders the session form model and manages the input
def new(request):
    if request.method == "POST":
        # This form data should sanitized first
        form = SessionForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("welcome")
    else:
        form = SessionForm()
    return render(request, "Main/new.html", {"form": form})
