from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	# Examples:
	url(r'^$', 'orgchartapp.views.home'),
	url(r'^employees/', 'orgchartapp.views.byEmployee'),	
	url(r'^orgchart/(?P<manager_id>\d+)$', 'orgchartapp.views.byReportingRelationship'),

	# Uncomment the admin/doc line below to enable admin documentation:
	url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
)
