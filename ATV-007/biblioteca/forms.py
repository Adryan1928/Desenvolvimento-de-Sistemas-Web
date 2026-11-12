from datetime import datetime

from django import forms
from .models import Autor, Livro

class AutorForm(forms.ModelForm):
    class Meta:
        model = Autor
        fields = ['nome', 'nacionalidade']
        labels = {
            'nome': 'Nome do Autor',
            'nacionalidade': 'Nacionalidade',
        }


class LivroForm(forms.ModelForm):
    class Meta:
        model = Livro
        fields = ['titulo', 'autores', 'ano_publicacao', 'disponivel', 'categorias']
        labels = {
            'titulo': 'Título do Livro',
            'autores': 'Autores',
            'ano_publicacao': 'Ano de Publicação',
            'disponivel': 'Disponível',
            'categorias': 'Categorias',
        }


    def clean_ano_publicacao(self):
        ano = self.cleaned_data.get('ano_publicacao')
        if ano > datetime.now().year:
            raise forms.ValidationError("O ano de publicação não pode ser maior que o ano atual.")
        return ano

    def clean_titulo(self):
        titulo = " ".join(str(self.cleaned_data.get('titulo')).split())
        if len(titulo) < 3:
            raise forms.ValidationError("O título do livro deve ter pelo menos 3 caracteres.")
        return titulo
