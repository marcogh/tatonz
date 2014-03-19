from django.conf.urls import patterns, include, url
from django.contrib import admin
from ffss.api import TrainResource

admin.autodiscover()

train_resource = TrainResource()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'tatonz.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include(train_resource.urls)),
)
