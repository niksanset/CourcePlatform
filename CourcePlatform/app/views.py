from django.shortcuts import render
from app.models import *
def course_list_view(request):
    courses = Course.objects.all()
    context = {'course_list': courses}
    return render(request,'course_list.html', context)

def course_create_view(request):
    return render(request,'course_create.html')

def course_update_view(request):
    return render(request,'course_update.html')

def course_delete_view(request):
    return render(request,'course_delete.html')

def course_detail_module_list_view(request):
    return render(request,'course_detail_module_list.html')

def module_create_view(request):
    return render(request,'module_create.html')

def module_delete_view(request):
    return render(request,'module_delete.html')

def module_update_view(request):
    return render(request,'module_update.html')

def module_detail_lesson_list_view(request):
    return render(request,'module_detail_lesson_list.html')

def lesson_create_view(request):
    return render(request,'lesson_create.html')


def lesson_delete_view(request):
    return render(request,'lesson_delete.html')

def lesson_update_view(request):
    return render(request,'lesson_update.html')

def lesson_detail_view(request):
    return render(request,'lesson_detail.html')

