from django.urls import path
from .views import listar_livros

app_name = 'biblioteca'
urlpatterns = [path('listar_livros/', listar_livros, name='listar_livros')
]