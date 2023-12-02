from django.shortcuts import render, redirect, get_object_or_404
from app.models import *
from app.forms import CourseForm,ModuleForm,LessonForm

def course_list_view(request):
    courses = Course.objects.all()
    context = {'course_list': courses}
    return render(request,'course_list.html', context)

def course_create_view(request):

    form = CourseForm()
    context = {'form': form}

    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        context['form'] = form
    
    return render(request,'course_create.html',context)

def course_update_view(request,pk):
    course = Course.objects.get(pk=pk)
    form = CourseForm(request.POST or None,instance=course)
    context = {'form': form,
               'course': course}
    if form.is_valid():
        form.save()

        return redirect('course_list')
    
    
    return render(request,'course_update.html',context)

def course_delete_view(request,pk):
     
    course = get_object_or_404(Course, pk=pk)
    context = {'course': course}
    if request.method == 'POST':
        course.delete()

        return redirect('course_list')
    


    return render(request,'course_delete.html',context)

def course_detail_module_list_view(request,pk):
    course = get_object_or_404(Course, pk=pk)
    module = Module.objects.all()
    context = {'course': course,
               'module_list':module}


    return render(request,'course_detail_module_list.html',context)

def module_create_view(request):
    form = ModuleForm()
    context = {'form': form}

    if request.method == 'POST':
        form = ModuleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        context['form'] = form

    return render(request,'module_create.html',context)

def module_delete_view(request,pk):
    module = get_object_or_404(Module, pk=pk)
    context = {'module': module}
    if request.method == 'POST':
        module.delete()

        return redirect('course_list')
    return render(request,'module_delete.html',context)

def module_update_view(request,pk):
    module = Module.objects.get(pk=pk)
    form = ModuleForm(request.POST or None,instance=module)
    context = {'form': form,
               'module': module}
    if form.is_valid():
        form.save()

        return redirect('course_list')
    return render(request,'module_update.html',context)

def module_detail_lesson_list_view(request,pk):
    module = get_object_or_404(Module, pk=pk)
    lesson = Lesson.objects.all()
    context = {'module': module,
               'lesson_list':lesson}


    return render(request,'module_detail_lesson_list.html',context)

def lesson_create_view(request):
    form = LessonForm()
    context = {'form': form}

    if request.method == 'POST':
        form = LessonForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('course_list')
        context['form'] = form

    return render(request,'lesson_create.html',context)


def lesson_delete_view(request,pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    context = {'lesson': lesson}
    if request.method == 'POST':
        lesson.delete()

        return redirect('course_list')
    return render(request,'lesson_delete.html',context)

def lesson_update_view(request,pk):
    lesson = Lesson.objects.get(pk=pk)
    form = LessonForm(request.POST or None,instance=lesson)
    context = {'form': form,
               'lesson': lesson}
    if form.is_valid():
        form.save()

        return redirect('course_list')
    return render(request,'lesson_update.html',context)

def lesson_detail_view(request,pk):
    lesson = get_object_or_404(Lesson, pk=pk)
    context = {'lesson': lesson,}
    return render(request,'lesson_detail.html',context)

