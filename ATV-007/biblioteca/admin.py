from django.contrib import admin
from .models import Livro, Categoria, Autor


class LivroAdmin(admin.ModelAdmin):
    list_display = ('titulo', 'autor', 'ano_publicacao', 'disponivel')
    list_filter = ('disponivel',)
    search_fields = ('titulo', 'autor__nome')
    filter_horizontal = ('categorias',)

class CategoriaAdmin(admin.ModelAdmin):
    list_display = ('nome',)
    search_fields = ('nome',)

class LivroInline(admin.TabularInline):
    model = Livro
    extra = 1
class AutorAdmin(admin.ModelAdmin):
    list_display = ('nome', 'nacionalidade')
    search_fields = ('nome', 'nacionalidade')
    inlines = [LivroInline]


admin.site.register(Livro, LivroAdmin)
admin.site.register(Categoria, CategoriaAdmin)
admin.site.register(Autor, AutorAdmin)