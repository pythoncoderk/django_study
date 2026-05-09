from django.shortcuts import render, redirect
from .models import Todo

def hello(request):

    if request.method == "POST":
        title = request.POST.get("title")

        if title:
            Todo.objects.create(title=title)

        return redirect("hello")

    todos = Todo.objects.all()

    context = {
        "todos": todos
    }

    return render(request, "hello/hello.html", context)


def toggle_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.completed = not todo.completed
    todo.save()

    return redirect("hello")


def delete_todo(request, todo_id):
    todo = Todo.objects.get(id=todo_id)
    todo.delete()

    return redirect("hello")