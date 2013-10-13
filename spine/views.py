from django.http import HttpResponse, render_to_response
from spine.models import Course

def file_upload(request, course_id):    
    if request.method == 'POST':
        form = FileUploadForm(request.POST, request.FILES)
        if form.is_valid():
            uploaded = form.cleaned_data['file_upload']
            mediaFile = Course(files=uploaded,
                                owner=request.user.profile,
                                creator=request.user.profile)
            mediaFile.save()

            return HttpResponseRedirect('/course/%s/' % course_id)#"%s/%d/%d/%s" % (settings.MEDIA_ROOT, course_id, user_id, filename)
    else:
        form = FileUploadForm()
    return render_to_response('course/file_upload.html', {'form':form,'course':course}, context_instance=RequestContext(request))
