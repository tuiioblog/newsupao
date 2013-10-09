from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'sampleapp.views.hora_actual', name='hora_actual'),
    url(r'^$', 'sampleapp.views.home', name='home'),
    url(r'^plus/(\d+)$', 'sampleapp.views.plus', name='plus'),
    url(r'^minus/(\d+)$', 'sampleapp.views.minus', name='minus'),
    url(r'^categoria/(\d+)$', 'sampleapp.views.categoria', name='categoria'),
    url(r'^add/$', 'sampleapp.views.add', name="add"),
    # url(r'^newsupao/', include('newsupao.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)
