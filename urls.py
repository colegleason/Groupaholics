from django.conf.urls.defaults import patterns, include, url
from groupaholic import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', views.main),
    url(r'^register/$', views.method_splitter, {'GET': views.register_get,'POST': views.register_post}),
    url(r'^profile/(?P<username>\w+)', views.profile),
    url(r'^account/edit/$', views.profile_edit),
    url(r'^account/login/$', 'django.contrib.auth.views.login', {'template_name': 'login.html'}),
    url(r'^account/logout/$', views.logout),
    url(r'^project/(?P<pk_id>\d+)$', views.project),
    url(r'^project/(?P<pk_id>\d+)/edit$', views.project),
                       url(r'^project/new$', views.method_splitter, {'GET': views.project_edit_get,'POST': views.project_edit_post}),
    url(r'^search$', include('haystack.urls')),
    # url(r'^cs_comp/', include('cs_comp.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),

)
