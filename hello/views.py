from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout, login
from django.contrib.auth.models import User

from .models import Todo


def signup(request):

    error_message = ""

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if not username or not password:
            error_message = "ユーザー名とパスワードを入力してください。"

        elif User.objects.filter(username=username).exists():
            error_message = "このユーザー名はすでに使われています。"

        elif len(password) < 8:
            error_message = "パスワードは8文字以上にしてください。"

        else:
            user = User.objects.create_user(
                username=username,
                password=password
            )

            login(request, user)

            return redirect("hello")

    context = {
        "error_message": error_message
    }

    return render(request, "hello/signup.html", context)


@login_required
def hello(request):

    if request.method == "POST":

        title = request.POST.get("title")

        if title:

            Todo.objects.create(
                title=title,
                user=request.user
            )

        return redirect("hello")

    search = request.GET.get("search")

    todos = Todo.objects.filter(
        user=request.user
    )

    if search:
        todos = todos.filter(
            title__icontains=search
        )

    todos = todos.order_by("-created_at")

    context = {
        "todos": todos,
        "search": search,
    }

    return render(
        request,
        "hello/hello.html",
        context
    )


@login_required
def toggle_todo(request, todo_id):

    todo = Todo.objects.get(
        id=todo_id,
        user=request.user
    )

    todo.completed = not todo.completed
    todo.save()

    return redirect("hello")


@login_required
def delete_todo(request, todo_id):

    todo = Todo.objects.get(
        id=todo_id,
        user=request.user
    )

    todo.delete()

    return redirect("hello")


@login_required
def edit_todo(request, todo_id):

    todo = Todo.objects.get(
        id=todo_id,
        user=request.user
    )

    if request.method == "POST":

        title = request.POST.get("title")

        if title:

            todo.title = title
            todo.save()

        return redirect("hello")

    context = {
        "todo": todo
    }

    return render(
        request,
        "hello/edit.html",
        context
    )


def logout_view(request):

    logout(request)

    return redirect("login")