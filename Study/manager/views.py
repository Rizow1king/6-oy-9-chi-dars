from django.core.handlers.wsgi import WSGIRequest
from django.shortcuts import render, get_object_or_404, redirect
from .models import *
from .forms import *


def home(request: WSGIRequest):
    lessons = Lesson.objects.all()
    context = {
        "lessons": lessons,
        'title': 'Barcha kurs hamda darslar'
    }
    return render(request, "index.html", context)


def lessons_by_courses(request: WSGIRequest, course_id):
    course = get_object_or_404(Course, id=course_id)
    lesson = Lesson.objects.filter(course_id=course_id)

    context = {
        'courses': [course],
        'lessons': lesson,
    }

    return render(request, 'index.html', context)


def lessons(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    context = {
        'lesson': lesson,
        'title': f'{lesson.name} - batafsil ma\'lumot'
    }
    return render(request, 'detail.html', context)


def course(request: WSGIRequest, lesson_id):
    lesson = get_object_or_404(Lesson, id=lesson_id)
    course = get_object_or_404(Course, id=lesson.course.id)
    course.views += 1
    course.save()
    context = {
        'lesson': lesson,
        'title': lesson.description
    }

    return render(request, 'detail.html', context)


def add_course(request: WSGIRequest):
    if request.method == 'POST':
        form = CourseForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            course = Course.objects.create(**form.cleaned_data)
            print(course, "qo'shildi!")
            return redirect('home')
    else:
        form = CourseForm()

    context = {
        "form": form
    }
    return render(request, 'add_course.html', context)


def add_lesson(request: WSGIRequest):
    if request.method == 'POST':
        form = LessonForm(data=request.POST, files=request.FILES)
        if form.is_valid():
            lesson = Lesson.objects.create(**form.cleaned_data)
            print(lesson, "qo'shildi!")
            return redirect('home')
    else:
        form = LessonForm()

    context = {
        "form": form
    }
    return render(request, 'add_lesson.html', context)


