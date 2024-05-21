from django.shortcuts import render, redirect
from django.contrib import messages

# Import todo form and models
from .forms import todoform
from .models import todo

###############################################

def index(request):
    # Fetches all To-Do items from the database and orders them by the date field.
    item_list = todo.objects.order_by("-date")
    
    # Checks if the request method is POST (indicating a form submission).
    if request.method == "POST":
        # Creates an instance of the TodoForm form, initialized with the data that was submitted in the POST request.
        form = todoform(request.POST)

        # If the form is valid, it saves the new To-Do item to the database and redirects to the todo URL.
        if form.is_valid():
            form.save()  # Creates a new record in the database with the data from the form.
            messages.info(request, "Item added")
            return redirect('todo')  # After saving the form data to the database, this redirects the user to the URL named todo.
    
    # Creates an empty form instance to be rendered on the page for the user to fill out.
    form = todoform()

    # Creates a context dictionary with the form, list of To-Do items, and a title.
    page = {
        "forms": form,  # 'forms' is a key and 'form' is a variable that represents an instance of the TodoForm.
        "list": item_list,  # 'item_list' is a variable that contains a list of todo items.
        "title": "TO-DO",  # The key "title" is assigned the string value "TO-DO".
    }
    return render(request, "todo/index.html", page)


# Function to remove item, it receives todo item_id as primary key from url.
def remove(request, item_id):
    # Fetches the To-Do item with the given item_id from the database.
    item = todo.objects.get(id=item_id)
    item.delete()
    messages.info(request, "Item removed")
    # Redirects the user back to the todo URL, typically the list of To-Do items.
    return redirect('todo')
