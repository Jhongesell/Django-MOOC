from django import forms
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit
from django.contrib.admin import widgets


from student_portal.models import Instructor, Course, Assignment

class SubmissionForm(forms.Form):
    docfile = forms.FileField(
        label='Select a file',
        help_text='max. 42 megabytes'
    )

class InstructorProfileForm(forms.ModelForm):
    class Meta:
        model = Instructor
        fields = [ 'first_name', 'last_name' ]
#	exclude = ("user")

class NewCourseForm(forms.ModelForm):
    class Meta:
	model = Course
	fields = ['name', 'department', 'description']
	exclude = ("instructor")

class NewAssignmentForm(forms.ModelForm):
    class Meta:
	model = Assignment
	fields = ['name', 'description', 'due_date','points_possible','submission_type']
	exclude = ("QUIZ", "EXAM", "HOMEWORK", "PROJECT", "SUBMISSION_TYPE_CHOICES", "course")

    def __init__(self, *args, **kwargs):
        super(NewAssignmentForm, self).__init__(*args, **kwargs)
        self.fields['due_date'].widget = widgets.AdminDateWidget()
