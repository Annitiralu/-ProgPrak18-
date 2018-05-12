from django.urls import path

from . import views

app_name = "ToDoSystem"

urlpatterns = {
    path("", views.index, name="index"),
    path("new/", views.new, name="new"),
    path("<int:task_id>/", views.change, name="change"),
    path("impressum/", views.impressum, name="impressum"),
}