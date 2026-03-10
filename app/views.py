from django.views.generic import TemplateView
from app.models import Portfolio, Service



class IndexView(TemplateView):
    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['portfolios'] = Portfolio.objects.all()
        context['services'] = Service.objects.all()
        return context
