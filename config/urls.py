from django.contrib import admin
from django.urls import path

from hello.views import hello, toggle_todo, delete_todo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', hello, name="hello"),
    path('toggle/<int:todo_id>/', toggle_todo, name="toggle_todo"),
    path('delete/<int:todo_id>/', delete_todo, name="delete_todo"),
]