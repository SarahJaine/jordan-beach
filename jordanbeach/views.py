from __future__ import unicode_literals

from django.views.generic import TemplateView, ListView
from .models import Teaching, Award, Poster, Talk, Publication


class HomeView(TemplateView):
    template_name = 'index.html'


class CVView(ListView):
    model = Publication
    template_name = 'cv.html'

    def get_context_data(self, **kwargs):
        context = super(CVView, self).get_context_data(**kwargs)
        context['mentor_list'] = Teaching.objects.filter(role='mentor')
        context['instructor_list'] = Teaching.objects.filter(role='instructor')
        context['award_list'] = Award.objects.all()
        context['poster_list'] = Poster.objects.all()
        context['talk_list'] = Talk.objects.all()
        return context
