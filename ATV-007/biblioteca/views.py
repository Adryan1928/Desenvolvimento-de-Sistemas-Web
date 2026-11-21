from django.urls import reverse_lazy
from django.views.generic import (
    CreateView,
    DeleteView,
    ListView,
    TemplateView,
    UpdateView,
    DetailView
)
from .models import Livro, Autor
from .forms import AutorForm, LivroForm


class LivroListView(ListView):
    model = Livro
    template_name = 'biblioteca/listar_livros.html'
    context_object_name = 'livros'

    def get_queryset(self):
        return Livro.objects.all().order_by("titulo")


class LivroCreateView(CreateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/criar_editar_livro.html'
    success_url = 'biblioteca:author_detail'
    pk_url_kwarg = 'livro_id'

    def get_success_url(self):
        return reverse_lazy(
            self.success_url,
            kwargs={'author_id': self.object.autores.first().id}
        )


class LivroUpdateView(UpdateView):
    model = Livro
    form_class = LivroForm
    template_name = 'biblioteca/criar_editar_livro.html'
    success_url = 'biblioteca:author_detail'
    pk_url_kwarg = 'livro_id'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['is_editing'] = True
        return context

    def get_success_url(self):
        return reverse_lazy(
            self.success_url,
            kwargs={'author_id': self.get_object().autores.first().id}
        )


class LivroDeleteView(DeleteView):
    model = Livro
    template_name = 'biblioteca/livro_confirm_delete.html'
    success_url = reverse_lazy('biblioteca:listar_livros')
    pk_url_kwarg = 'livro_id'


class SobreView(TemplateView):
    template_name = 'biblioteca/sobre.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['total_livros'] = Livro.objects.all().count()
        context['livros_disponiveis'] = Livro.objects.filter(disponivel=True).count()
        return context


class AuthorDetailView(DetailView):
    model = Autor
    template_name = 'biblioteca/author_detail.html'
    context_object_name = 'autor'
    pk_url_kwarg = 'author_id'


class AuthorCreateView(CreateView):
    model = Autor
    form_class = AutorForm
    template_name = 'biblioteca/criar_editar_livro.html'
    success_url = 'biblioteca:author_detail'

    def get_success_url(self):
        return reverse_lazy(
            self.success_url,
            kwargs={'author_id': self.object.id}
        )
