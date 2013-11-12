from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'blog.views.home', name='home'),
    url(r'^blog/(?P<slug>[-\w]+)/$', 'blog.views.blog', name='blog'),
    url(r'^admin/', include(admin.site.urls)),
)
