from django.urls import path
from .views import (
    LivroCreateView,
    LivroDeleteView,
    LivroListView,
    LivroUpdateView,
    SobreView,
    AuthorCreateView,
    AuthorDetailView
)

app_name = 'biblioteca'
urlpatterns = [
    path('listar_livros/', LivroListView.as_view(), name='listar_livros'),
    path('author/<int:author_id>/', AuthorDetailView.as_view(), name='author_detail'),
    path('criar_autor/', AuthorCreateView.as_view(), name='criar_autor'),
    path('criar_editar_livro/', LivroCreateView.as_view(), name='criar_livro'),
    path('criar_editar_livro/<int:livro_id>/', LivroUpdateView.as_view(), name='editar_livro'),
    path('criar_editar_livro/<int:livro_id>/excluir/', LivroDeleteView.as_view(), name='excluir_livro'),
    path('sobre/', SobreView.as_view(), name='sobre'),
]