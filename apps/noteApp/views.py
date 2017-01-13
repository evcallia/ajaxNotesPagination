from django.shortcuts import render, redirect, HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
# from django.contrib import messages
# from .forms import RegistrationForm
from .models import Note
import math
#CONTROLLER
#Create your views here.
def index(request):
    return redirect(reverse("note:showNotes"))

def showNotes(request):
    pages = int(math.ceil(len(Note.objects.all()) / 5.0))
    return render(request, 'noteApp/notes.html', {'notes': Note.objects.all()[:5], 'pages': range(0, pages)})

def create(request):
    print request.POST
    Note.objects.create(title = request.POST['title'], description = request.POST['description'])
    return redirect(reverse("note:showNotes"))

def update(request, id):
    note = Note.objects.get(id = id)
    note.title = request.POST['title']
    note.description = request.POST['description']
    note.save()
    return redirect(reverse("note:showNotes"))

def delete(request, id):
    Note.objects.get(id=id).delete()
    return redirect(reverse("note:showNotes"))

def pages(request, number, page):
    pages = int(math.ceil(len(Note.objects.all()) / (int(number) * 1.0)))

    start = (int(page) * int(number)) - int(number)
    end = start + int(number)
    return render(request, 'noteApp/notes.html', {'notes': Note.objects.all()[start:end], 'pages': range(0, pages)})








#
