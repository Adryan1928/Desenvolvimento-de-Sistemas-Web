from django.contrib import admin
from .models import Livro, Categoria, Autor


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'ano_publicacao', 'disponivel')
    list_filter = ('disponivel',)
    search_fields = ('titulo',)
    filter_horizontal = ('categorias',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

# class AutorLivroInline(admin.TabularInline):
#     model = Autor.livros.through
#     extra = 1
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome', 'nacionalidade')
    # inlines = [AutorLivroInline]


admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)