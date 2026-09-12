from django.urls import path
from . import views

app_name = 'estudio'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('portfolio/', views.PortfolioView.as_view(), name='portfolio'),
]
