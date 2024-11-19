from django.http import HttpResponse
from .models import Todo
from django.shortcuts import redirect, render, get_object_or_404

# Home view
def home(request):
    return render(request, "home.html")

# Add a new todo
def add(request):
    if request.method == "POST":
        todo_name = request.POST.get("todo_name", "").strip()
        todo_description = request.POST.get("todo_description", "").strip()

        if not todo_name or not todo_description:
            return HttpResponse("Both name and description are required.", status=400)

        try:
            Todo.objects.create(todo_name=todo_name, todo_description=todo_description)
            return redirect("todo_list")  # Use named URL patterns for better maintainability
        except Exception as e:
            return HttpResponse(f"Error saving todo: {str(e)}", status=500)

    return render(request, "add.html")

# Display the list of todos
def todo_list(request):
    todos = Todo.objects.all()

    if not todos.exists():
        return HttpResponse("No todos found.", status=404)

    return render(request, "list.html", {"todos": todos})

# Delete a todo
def delete(request, id):
    try:
        todo = get_object_or_404(Todo, id=id)  # Better error handling for invalid IDs
        todo.delete()
        return redirect("todo_list")
    except Exception as e:
        return HttpResponse(f"Error deleting todo: {str(e)}", status=500)

# Update a todo
def update(request, id):
    todo = get_object_or_404(Todo, id=id)  # Better error handling for invalid IDs

    if request.method == "POST":
        todo_name = request.POST.get("name", "").strip()
        todo_description = request.POST.get("desc", "").strip()

        if not todo_name or not todo_description:
            return HttpResponse("Both name and description are required.", status=400)

        try:
            todo.todo_name = todo_name
            todo.todo_description = todo_description
            todo.save()
            return redirect("todo_list")
        except Exception as e:
            return HttpResponse(f"Error updating todo: {str(e)}", status=500)

    return render(request, "update.html", {"todo": todo})
