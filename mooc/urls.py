from django.conf.urls import patterns, include, url
from django.contrib import admin
admin.autodiscover()

from mooc.views import login_view,student_view,instructor_view,login_fields
from spine.views import file_upload

urlpatterns = patterns('',
    url(r'^login/$', login_fields),
    url(r'^login/next=?$', login_view),                    
    url(r'^student/$', student_view),
    url(r'^instructor/$', instructor_view),
    url(r'^course/{/s}/files$', file_upload),
#    url(r'^course/files/$', file_upload),
# Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
