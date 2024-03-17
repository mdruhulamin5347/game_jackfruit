from django.shortcuts import render,redirect
from .models import *
from django.contrib import messages
from random import randint
# Create your views here.


def HOME(request):
    if request.method == 'POST':
        name = request.POST.get('name')
        if HOME_MODEL.objects.filter(name=name).exists():
            messages.error(request, 'The name already exists in the list !')
        else:
            nameSave = HOME_MODEL(name=name)
            nameSave.save() 
    obj = HOME_MODEL.objects.all()
    return render(request, 'home.html', {'obj':obj})


def CONGRATULATION(request):
    obj = HOME_MODEL.objects.all()
    obj_count = HOME_MODEL.objects.all().count()
    if obj_count == 0:
        messages.error(request,'Please add your information first to the list !')
        return redirect('home')
    else:
        if request.method == 'POST':
            choice_count = request.POST.get('choice_count')
            choice_countt=int(choice_count)
            if int(obj_count) < int(choice_count):
                messages.error(request, f'''Choose numbers smaller than {obj_count + 1}  !''')
                return redirect('home')
            else:
                name_listt = []
                unique_indices = set()
                if obj:
                    for i in obj:
                        name_listt.append(i.name)
                name_list=[]
                while len(name_list) < choice_countt:
                    random_index = randint(0, obj_count - 1)
                    if random_index not in unique_indices:
                        unique_indices.add(random_index)
                        random_name = name_listt[random_index].title()
                        name_list.append(random_name)
                name_string = ' , '.join(name_list)
                names_string = name_string.title()
    return render(request, 'congratulations.html',{'names_string':names_string})


def DELETE(request):
    obj = HOME_MODEL.objects.all()
    obj.delete()
    messages.success(request,'Your data has been successfully deleted !')
    return redirect('home')