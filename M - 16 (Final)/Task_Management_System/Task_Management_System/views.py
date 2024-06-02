from django.shortcuts import render
from task.models import TaskModel
def home(request):
    return render(request, 'base.html')

def show_task(request):
    tasks =  TaskModel.objects.all()
    # print(tasks)
    # for i in tasks:
    #     print(i.taskTitle)
    #     for j in i.category.all():
    #         print(j)
    #     print()
    return render(request, 'show.html', {'tasks':tasks})