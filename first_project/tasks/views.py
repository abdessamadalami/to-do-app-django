from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import *
from .forms import *
# Create your views here.
def index(request):
    tasks = Tasks.objects.all()
    form = TasksForm()
    if request.method == 'POST':
        form = TasksForm(request.POST)
        if form.is_valid():
            form.save()
        return redirect('tasks/')

    context = {'tasks':tasks, 'form':form }
    return render(request,'tasks/list.html',context)

def updateTasks(request,pk):
    tasks =Tasks.objects.get(id=pk)
    form = TasksForm(instance=tasks)
    if request.method == 'POST':
        form = TasksForm(request.POST , instance=tasks)
        if form.is_valid():
            form.save()
        return redirect('/tasks')

    context = {'forms':form}
    return render(request, 'tasks/update.html',context)


def deleteTasks(request,pk):
    item =Tasks.objects.get(id=pk)
    if request.method == 'POST':
        item.delete()
    context = {'item':item }
    return render(request, 'tasks/delete.html',context)
