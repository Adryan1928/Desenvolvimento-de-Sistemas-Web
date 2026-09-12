from django.views.generic import TemplateView

class IndexView(TemplateView):
    template_name = 'estudio/index.html'

class PortfolioView(TemplateView):
    template_name = 'estudio/portfolio.html'