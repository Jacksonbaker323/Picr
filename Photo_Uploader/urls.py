from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'Picr.views.home', name='home'),
    url(r'^gallery/', 'Picr.views.gallery', name='gallery'),
    url(r'^submitted/', 'Picr.views.submitted', name='submitted'),
    url(r'^search/', 'Picr.views.search', name='search'),
    #url(r'^gallery/', Photo_Uploader.views.)
    url(r'^admin/', include(admin.site.urls)),
)
