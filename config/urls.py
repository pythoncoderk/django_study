from django.contrib import admin
from django.urls import path
from django.contrib.auth import views as auth_views

from hello.views import (
    hello,
    toggle_todo,
    delete_todo,
    edit_todo,
    logout_view,
    signup
)

urlpatterns = [
    path('admin/', admin.site.urls),

    path('hello/', hello, name="hello"),

    path(
        'toggle/<int:todo_id>/',
        toggle_todo,
        name="toggle_todo"
    ),

    path(
        'delete/<int:todo_id>/',
        delete_todo,
        name="delete_todo"
    ),

    path(
        'edit/<int:todo_id>/',
        edit_todo,
        name="edit_todo"
    ),

    path(
        'login/',
        auth_views.LoginView.as_view(
            template_name='hello/login.html'
        ),
        name='login'
    ),

    path(
        'logout/',
        logout_view,
        name='logout'
    ),

    path(
        'signup/',
        signup,
        name='signup'
    ),
]