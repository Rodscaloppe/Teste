from django.conf.urls import patterns, include, url
from django.contrib import admin

urlpatterns = patterns('',
    url(r'^drca/', include('DRCA.urls')),
    url(r'^admin/', include(admin.site.urls)),
)