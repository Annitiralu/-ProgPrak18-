from django.shortcuts import render, redirect, get_object_or_404
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import PostForm, EditForm


# Create your views here.
def index(request):
    task_list = Task.objects.filter(done=False).order_by("deadline")
    context = {"task_list": task_list}
    return render(request, "ToDoSystem/index.html", context)


def new(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            task = form.save(commit=False)
            task.progress = "0"
            task.done = False
            task.save()
            return redirect("ToDoSystem:index")
    else:
        form = PostForm()
    return render(request, "ToDoSystem/new.html", {"form": form})


def change(request, task_id):
    task = get_object_or_404(Task, pk=task_id)
    if request.method == "POST":
        form = EditForm(request.POST, instance=task)
        if form.is_valid():
            form.save()
            return redirect("ToDoSystem:index")
    else:
        form = EditForm(instance=task)
    return render(request, "ToDoSystem/change.html", {'form': form})


def impressum(request):
    return render(request, "ToDoSystem/impressum.html")
