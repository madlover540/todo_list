from datetime import date
from django.http import Http404
from django.shortcuts import redirect, render
from todo.forms import TodoListForm

from todo.models import TodoListModel

# Create your views here.


def index(request):
    model =TodoListModel()
    form = TodoListForm()
    listview = TodoListModel.objects.all()
    if request.method == 'POST':
        form = TodoListForm(request.POST)
        if form.is_valid():
            newtask =form.cleaned_data['task']
            updatedform = TodoListModel(task = newtask)
            updatedform.save()
            for task in TodoListModel.objects.values_list('task', flat=True).distinct():
                TodoListModel.objects.filter(pk__in=TodoListModel.objects.filter(task=newtask).values_list('id', flat=True).order_by('id')[1:]).delete()
            return render (request, 'todo/index.html', { 'form':form, 'listview':listview})
        else:
            return render(request, 'todo/alert.html')

    return render(request, 'todo/index.html', {'form':form , 'listview':listview})


def deletetask (request, pk):
    model = TodoListModel.objects.get(id=pk)
    model.delete()
    return redirect('/')
