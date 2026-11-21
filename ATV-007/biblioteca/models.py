from django.db import models
from django.core.validators import MinLengthValidator
from .validators import validate_ano_publicacao, validate_paginas, validate_isbn

class Autor(models.Model):
    nome = models.CharField(max_length=200)
    nacionalidade = models.CharField(max_length=200, null=True, blank=True)

    class Meta:
        ordering = ["nome"]
        verbose_name_plural = 'autores'

    def __str__(self):
        return self.nome

class Categoria(models.Model):
    nome = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.nome

class Livro(models.Model):
    titulo = models.CharField(max_length=200, validators=[MinLengthValidator(3)])
    # autor = models.ForeignKey(Autor, related_name='books', on_delete=models.CASCADE, null=True, blank=True)
    autores = models.ManyToManyField(Autor, related_name='livros')
    ano_publicacao = models.IntegerField(validators=[validate_ano_publicacao])
    disponivel = models.BooleanField(default=True)
    categorias = models.ManyToManyField(Categoria, blank=True)
    paginas = models.PositiveIntegerField(null=True, blank=True, validators=[validate_paginas])
    isbn = models.CharField(max_length=13, null=True, blank=True, validators=[validate_isbn])

    def __str__(self):
        return self.titulo

    def get_autores(self):
        return "\n".join([a.nome + ", " for a in self.autores.all()])
