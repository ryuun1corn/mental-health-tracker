from django.shortcuts import render, redirect
from main.forms import MoodEntryForm
from main.models import MoodEntry

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