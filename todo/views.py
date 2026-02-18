from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Todo


def todo_list(request):
    if request.method == "POST":
        body = request.POST.get("body")
        duration = request.POST.get("duration")
        duration_type = request.POST.get("duration_type")
        status = request.POST.get("status")

        todo = Todo.objects.create(
            body = body,
            duration = duration,
            duration_type = duration_type,
            status = status
        )
        return redirect("todo_list")
    
    todos = Todo.objects.all()
    
    return render(request,"todos.html", context={"todos":todos})