from django.urls import path
from .views import listar_livros, author_detail

app_name = 'biblioteca'
urlpatterns = [
    path('listar_livros/', listar_livros, name='listar_livros'),
    path('author/<int:author_id>/', author_detail, name='author_detail')
]