from django.shortcuts import render

tasks = ["Go job", "Write", "read", "Wash", "make"]

# Create your views here.

def index(request):
    return render(request, "tasks/index.html", {
        "tasks": tasks
    })
