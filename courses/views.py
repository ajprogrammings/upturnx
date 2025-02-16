from django.shortcuts import render

def courses_list(request):
    return render(request, 'courses/courses.html')
