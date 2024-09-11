from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core import serializers
from main.forms import MoodEntryForm
from main.models import MoodEntry

def show_xml(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("xml", data), content_type="application/xml")

def show_json(request):
    data = MoodEntry.objects.all()
    return HttpResponse(serializers.serialize("json", data), content_type="application/json")

def create_mood_entry(request):
    form = MoodEntryForm(request.POST or None)
    
    if form.is_valid() and request.method == "POST":
        form.save()
        return redirect("main:show_main")
    
    context = {
        "form": form
    }
    
    return render(request, "create_mood_entry.html", context)

def show_main(request):
    mood_entries = MoodEntry.objects.all()
    context = {
        'npm' : '2306215160',
        'name': 'Yudayana Arif Prasojo',
        'class': 'PBP D',
        'mood_entries': mood_entries
    }

    return render(request, "main.html", context)