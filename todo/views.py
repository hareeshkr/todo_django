from django.shortcuts import render
from django.http import HttpResponseRedirect
from .models import TodoList
from .forms import CreateTodo


def base(response):
    return render(response, "todo/base.html", {})

def home(request):
    ls = TodoList.objects
    if request.method == "POST":
        check = int(request.POST.getlist("check")[0])
        print(check)
        t = ls.get(id=check)
        t.delete()

    return render(request, "todo/home.html", {"items": ls.all()})

def create(response):
    if response.method == "POST":
        form = CreateTodo(response.POST)
        if form.is_valid():
            n = form.cleaned_data["item"]
            t = TodoList(item = n)
            t.save()
        return HttpResponseRedirect("../")
    else:
        form = CreateTodo()
    return render(response, "todo/create.html", {"forms": form})
