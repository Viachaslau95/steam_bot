from django.views.generic import TemplateView


class GiveMoney(TemplateView):
    template_name = 'index.html'
