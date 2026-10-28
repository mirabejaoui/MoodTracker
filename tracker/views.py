from django.http import HttpResponse
from django.shortcuts import render
from datetime import datetime

def home(request):
    return render(request, 'home.html')

def entry_list(request):
    entries = [
        {
            "pk": 1,
            "mood": "Great",
            "date": datetime(2026, 10, 1),
            "intensity": 9,
            "note": "Had a very productive day and accomplished most of my goals.",
            "tags": [{"pk": 1, "name": "work"}, {"pk": 3, "name": "productive"}, {"pk": 4, "name": "motivation"}]
        },
        {
            "pk": 2,
            "mood": "Good",
            "date": datetime(2026, 10, 2),
            "intensity": 7,
            "note": "A good day. I managed to finish my tasks and had some time to relax.",
            "tags": [{"pk": 1, "name": "work"}, {"pk": 2, "name": "relaxation"}]
        },
        {
            "pk": 3,
            "mood": "okay",
            "date": datetime(2026, 10, 3),
            "intensity": 5,
            "note": "Nothing special today. Everything went normally.",
            "tags": [{"pk": 5, "name": "normal-day"}]
        }
    ]
    return render(request, "moods/entry_list.html", {"entries": entries})

def entry_create(request):
    return render(request,"moods/entry_form.html")

def entry_detail(request, id):
    return HttpResponse(f"Detail of entry #{id}")

def entry_edit(request, id):
    return HttpResponse(f"Edit form for entry #{id}")

def entry_delete(request, id):
    return HttpResponse(f"Confirm deletion of entry #{id}")

def tag_list(request):
    tags = [
        {"pk": 1, "name": "work"},
        {"pk": 2, "name": "relaxation"},
        {"pk": 3, "name": "productive"},
        {"pk": 4, "name": "motivation"},
        {"pk": 5, "name": "normal-day"},
    ]
    return render(request, "tags/tag_list.html", {"tags": tags})

def tag_detail(request, slug):
    return HttpResponse(f"Entries tagged'{slug}'")

def category_list(request):
    return HttpResponse("List of mood categories")

def stats(request):
    total_entries = 3
    average_mood = 3.6
    average_intensity = 6
    current_streak = 12
    return render(request, "moods/stats.html",
    {"total_entries": total_entries, "average_mood": average_mood,
     "average_intensity": average_intensity, "current_streak": current_streak })