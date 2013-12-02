from django.shortcuts import render_to_response, render, redirect
from django.contrib.auth.decorators import login_required
from django.http import HttpResponseRedirect, HttpResponse
from django.core.urlresolvers import reverse
from django.template import RequestContext
from django.conf import settings
from django.core.servers.basehttp import FileWrapper
from registration.backends.simple.views import RegistrationView
from django.views.generic.edit import UpdateView
from django.core.context_processors import csrf

import os
import mimetypes

from instructor_portal.forms import SubmissionForm, InstructorProfileForm
from student_portal.views import get_assignment, get_assignments, get_course, get_lectures
from student_portal.models import *

class InstructorProfileEditView(UpdateView):
    model = Instructor
    form_class = InstructorProfileForm
    template_name = "instructor_portal/edit_profile.html"

def get_object(self, queryset=None):
    return Instructor.objects.get_or_create(user=self.request.user)[0]

def get_success_url(self):
    return "/instructor/" #TODO change this to send a user to a nice updated profile page

def instructor_about(request):
    return render(request, 'about.html')

def lecture(request):
    my_video = 'http://www.youtube.com/watch?v=0d0uu7MW__U'
    context = {'my_video': my_video}
    return render_to_response('instructor_portal/dashboard.html', context)

def get_instructor_from_user(user):
    ls = [instructor for instructor in Instructor.objects.all() if instructor.user == user]
    if ls:
	return ls[0]
    else:
	instructor = Instructor(user=user)
	instructor.save()
	return instructor

def get_separated_course_list(instructor, course_list):
    taught_courses = instructor.course_set.all()#TODO error after login 
    not_taught_courses = []
    for course in course_list:
	if not course.id in map(lambda course: course.id, taught_courses):
	    not_taught_courses.append(course)
    return taught_courses, not_taught_courses

@login_required(login_url='/accounts/login/')
def dashboard(request):
    """
    If users are authenticated, direct them to the main page. Otherwise, take
    them to the login page.
    """
    taught_courses,not_taught_courses = get_separated_course_list(get_instructor_from_user(request.user), Course.objects.all())
    context = {'user': request.user,
               'taught_courses':taught_courses}
    return render_to_response('instructor_portal/dashboard.html', context)

def display_courses(request):
    course_list = Course.objects.all()
    taught_courses,not_taught_courses = get_separated_course_list(get_instructor_from_user(request.user), course_list)
    print(taught_courses)
    teacher = True
    context = {'taught_courses': taught_courses,
	   'course_list':course_list,
	   'teacher':teacher}
    return render(request, 'courses.html', context)

def course_dashboard(request, course_id):
    course = get_course(int(course_id))
    assignments = get_assignments(course)
    course_materials = CourseMaterial.objects.all().filter(course=course)
    context = {'assignments' : assignments,
<<<<<<< HEAD
	 'course' : course}
=======
               'course' : course,
               'course_materials' : course_materials}
>>>>>>> e7e9b7292e53a2c7e0ae0a8c4c68473cbc6e2aea
    return render(request, 'instructor_portal/course_dashboard.html', context)

def assignment_dashboard(request, course_id, assignment_id):
    course = Course.objects.all().get(id=int(course_id))
    assignments = Assignment.objects.all().filter(course=course)
    assignment = Assignment.objects.all().get(id=int(assignment_id))
    subs = Submission.objects.all().filter(assignment=assignment)
    context = {'submissions' : subs,
<<<<<<< HEAD
    	   'assignments' : assignments,
	   'course' : course}
    context.update(csrf(request))
    if request.method == 'POST':
	print "in post"
	p = request.POST
	print p
	sub = Submission.objects.all().get(id=int(p['submission_id']))
	sub.grade = float(p['newgrade'])
	sub.save()
	return render(request, 'instructor_portal/assignment_dashboard.html',context)
=======
               'assignment' : assignment,
               'assignments' : assignments,
               'course' : course}
    context.update(csrf(request))
    if request.method == 'POST':
        print "in post"
        p = request.POST
        sub = Submission.objects.all().get(id=int(p['submission_id']))
        if p['newgrade']:
            sub.grade = float(p['newgrade'])
        sub.remarks = p['newremarks']
        sub.save()
        return render(request, 'instructor_portal/assignment_dashboard.html',context)
>>>>>>> e7e9b7292e53a2c7e0ae0a8c4c68473cbc6e2aea
    return render(request, 'instructor_portal/assignment_dashboard.html', context)

@login_required(login_url='/accounts/login/') 
def download_submission(request, course_id, assignment_id, submission_id):
    sub = Submission.objects.all().get(id=int(submission_id))
    print sub.id
    dirlist = sub.docfile.name.split(os.sep)
    while dirlist[0] != 'media':
	dirlist.pop(0)
    print dirlist
    print dirlist[-1]
    type, _ = mimetypes.guess_type(dirlist[-1])
    print type
    f = open(sub.docfile.name, "r")
    response = HttpResponse(FileWrapper(f), content_type=type)
    response['Content-Disposition'] = 'attachment; filename=' + dirlist[-1]
    return response

def display_course_info(request, course_department, course_id):
    course = get_course(int(course_id))
    lecture_list = get_lectures(course)
    assignment_list = get_assignments(course)
    print assignment_list
    if request.user.is_authenticated():
	instructor = Instructor.objects.all().get(id=request.user.instructor.id)
	taught_courses, not_taught_courses = get_separated_course_list(instructor, Course.objects.all())
	is_taught = course in taught_courses
    
    is_enrolled = False
    return render(request, 'course_info.html', { 'course' : course,
<<<<<<< HEAD
					     'is_enrolled': is_enrolled,
					     'lecture_list' : lecture_list,
					     'assignment_list': assignment_list,
					     'is_student' : False})
def course_grades(request, course_id):
    assignments = Course.objects.get(id=course_id).assignment_set.all().order_by('date')
    students = Course.objects.get(id=course_id).student_set.all().order_by('last_name')
    grade_chart[0][0] = "    "
    for i in range(1,assignment.length()):
	grade_chart[i][0] = assignments[i]







    for assignment in assignments:
	for submission in assignment.submission_set.all():
	    submissions[assignment] = (submission.submitter, submission.grade)
    context = {'students': students,
		'assignments': assignments
		'submissions': submissions}
    return render(request, 'instructor_portal/course_grades.html', context)
=======
                                                 'is_enrolled': is_enrolled,
                                                 'lecture_list' : lecture_list,
                                                 'assignment_list': assignment_list,
                                                 'is_student' : False})

def delete_course_material(request, course_id, course_mat_id):
    cm = CourseMaterial.objects.all().get(id=int(course_mat_id))
    os.remove(cm.file.name)
    cm.delete()
    return HttpResponseRedirect('/instructor/' + course_id + '/dashboard')

def download_course_material(request, course_id, course_mat_id):
    cm = CourseMaterial.objects.all().get(id=int(course_mat_id))
    dirlist = cm.file.name.split(os.sep)
    print dirlist
    while dirlist[0] != 'media':
        dirlist.pop(0)
    type, _ = mimetypes.guess_type(dirlist[-1])
    f = open(cm.file.name, "r")
    response = HttpResponse(FileWrapper(f), content_type=type)
    response['Content-Disposition'] = 'attachment; filename=' + dirlist[-1]
    return response

def handle_uploaded_course_material(file, course_department, course_id, cm_description, user):
    if file:
        cm = CourseMaterial(course = get_course(int(course_id)),
                            description = cm_description)
        cm.save()
                            
        directory = settings.MEDIA_ROOT+ '/' + course_department + '/' + unicode(course_id) +  '/course_material/'
        if not os.path.exists(directory):
            os.makedirs(directory)
        _, fileExtension = os.path.splitext(file.name)
        filename = course_department + '_' + unicode(course_id) + '_' + unicode(cm.id)  + fileExtension
        print filename
        destination = open(directory+filename, 'wb+')
        for chunk in file.chunks():
            destination.write(chunk)
        destination.close()
        cm.file.name = directory+filename
        cm.save()
        
def upload_course_material(request, course_id):
    if request.method == 'POST':
        a = request.POST #the post dict
        form = SubmissionForm(request.POST, request.FILES)
        if form.is_valid():
            course = get_course(int(course_id))
            handle_uploaded_course_material(request.FILES['file'], course.department, course.id, a['description'], request.user)
            return HttpResponseRedirect('/instructor/' + course_id + '/dashboard')

    else:
        form = SubmissionForm()
    
    context = {'form' : form}
    context.update(csrf(request))
    return render_to_response('upload.html', context)
>>>>>>> e7e9b7292e53a2c7e0ae0a8c4c68473cbc6e2aea
