from django.shortcuts import render, get_object_or_404
from .models import Livro, Autor

def listar_livros(request):
    livros = Livro.objects.all()
    return render(request, 'biblioteca/listar_livros.html', {'livros': livros})

def author_detail(request, author_id):
    autor = get_object_or_404(Autor, id=author_id)

    return render(request, 'biblioteca/author_detail.html', {'autor': autor})
