from django.urls import reverse_lazy
from django.views.generic import TemplateView, FormView
from app.form import ContactForm



class IndexView(TemplateView):
    template_name = 'index.html'

class ContactView(FormView):
    form_class = ContactForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        form.save()
        return super().form_valid(form)