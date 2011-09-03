from django.conf.urls.defaults import patterns, include, url
from groupaholic import views
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', views.main),
    url(r'^register$', views.register),
    url(r'^profile/(?P<username>)\w+', views.profile),
    url(r'^account/edit$', views.profile_edit),
    url(r'^project/(?P<pk_id>)\d+$', views.project),
    url(r'^project/(?P<pk_id>)\d+/edit$', views.project_edit),
    url(r'^search$', views.search),
    # url(r'^cs_comp/', include('cs_comp.foo.urls')),
    # Uncomment the admin/doc line below to enable admin documentation:
     url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     url(r'^admin/', include(admin.site.urls)),
	 
	 #Registration form script url
	 url(r'^registerScript/', views.register_script),
	 
	 #Registration success page
	 url(r'^registerSuccess', views.register_success),

)
