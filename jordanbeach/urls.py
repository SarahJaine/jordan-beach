from django.conf.urls import include, url
from django.contrib import admin

from jordanbeach.views import HomeView, PublicationList, CVView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^publications/$', PublicationList.as_view(), name='publications'),
    url(r'^cv/$', CVView.as_view(), name='cv'),
    url(r'^admin/', include(admin.site.urls)),
]
