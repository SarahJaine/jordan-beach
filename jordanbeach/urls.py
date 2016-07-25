from django.conf.urls import include, url
from django.contrib import admin

from jordanbeach.views import HomeView, CVView

urlpatterns = [
    url(r'^$', HomeView.as_view(), name='home'),
    url(r'^cv/$', CVView.as_view(), name='cv'),
    url(r'^admin/', include(admin.site.urls)),
]
