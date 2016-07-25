from __future__ import unicode_literals

from django.views.generic import TemplateView, ListView
from .models import Publication


class HomeView(TemplateView):
    template_name = 'index.html'


class CVView(ListView):
    model = Publication
    template_name = 'cv.html'
