from django.shortcuts import render
from django.http import HttpResponse, HttpResponseRedirect
from .models import Task
from .forms import PostForm


# Create your views here.
def index(request):
    task_list = Task.objects.order_by("-deadline")
    context = {"task_list": task_list}
    return render(request, "ToDoSystem/index.html", context)


def new(request):
    form = PostForm()
    return render(request, "ToDoSystem/new.html", {"form": form})


def change(request, task_id):
    return render(request, "ToDoSystem/change.html")


def impressum(request):
    return render(request, "ToDoSystem/impressum.html")
