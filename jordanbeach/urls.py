from django.conf.urls import include, url
from django.contrib import admin

from jordanbeach.views import HomeView, PublicationList

urlpatterns = [
    # Examples:
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^publications/$', PublicationList.as_view(), name='publications'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^admin/', include(admin.site.urls)),
]
