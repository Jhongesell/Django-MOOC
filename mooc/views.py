from django.http import HttpResponse, HttpResponseRedirect
from django.template import RequestContext
from django.shortcuts import render, render_to_response, redirect

from student_portal.models import Course, Student
from student_portal.views import get_separated_course_list, get_student_from_user, enroll_courses

def index(request):
    return render(request, 'index.html')

def about(request):
    return render(request, 'about.html')

def get_course(course_id):
    course_list = Course.objects.all()
    for course in course_list:
        if (course.id == course_id):
            return course

def display_course_info(request, course_id):
    if request.method == 'POST':
        if not request.user.is_authenticated():
            return redirect('/accounts/login')
        enroll_courses(request)

    course = get_course(int(course_id))
    if request.user.is_authenticated():
        student = get_student_from_user(request.user)
        enrolled_ls, not_enrolled_ls = get_separated_course_list(student, Course.objects.all())
        is_enrolled = course in enrolled_ls

    else:
        is_enrolled = False
        
    print "display_course_info: got "
    print course
    print course.id
    return render(request, 'course_info.html', { 'course' : course,
                                                 'is_enrolled': is_enrolled})
