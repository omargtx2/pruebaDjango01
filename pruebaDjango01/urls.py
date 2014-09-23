from django.conf.urls import patterns, include, url
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'pruebaDjango01.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    #url(r'^$','app1.views.inicio'),
     #url(r'^$','app1.views.followers'),
     url(r'^admin/', include(admin.site.urls)),
    

    #url(r'^sign-in/$', 'sign_in', name='sign_in'),
     url(r'^$', 'app1.views.index', name='index'),
     url(r'^followers/$', 'app1.views.followers', name='followers'),
)
