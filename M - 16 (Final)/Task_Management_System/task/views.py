from django.shortcuts import render,redirect
from . import forms
from . import models
# Create your views here.
def TaskViews(request):
    # taskform = forms.TaskForms()
    # return render(request, 'task.html',{'taskform':taskform})
    if request.method == 'POST':
        taskform = forms.TaskForms(request.POST)
        if taskform.is_valid():
            taskform.save()
            return redirect('show_tasks')
    else:
        taskform = forms.TaskForms()
        return render(request, 'task.html',{'taskform':taskform})
    

def EditTask(request,id):
    task_id = models.TaskModel.objects.get(pk=id)
    taskform = forms.TaskForms(instance=task_id)
    print(task_id)
    if request.method == 'POST':
        taskform = forms.TaskForms(request.POST, instance=task_id)
        if taskform.is_valid():
            taskform.save()
            return redirect('show_tasks')
    # else:
    #     taskform = forms.TaskForms()
    return render(request, 'task.html',{'taskform':taskform})


def DeleteTask(request,id):
    task_id = models.TaskModel.objects.get(pk=id)
    task_id.delete()
    return redirect("show_tasks")
    