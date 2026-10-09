# models.CASCADE - Justificativa de escolha:
Quando alguém tentar apagar um autor que tem livros, os livros precisam ser apagados também. Essa associação faz sentido porque os livros obrigatoriamente precisam de um autor.


1. Que dados se perdem quando a migração é revertida? Por quê?
A migração não pode ser reliazada, já que autor é um campo obrigatório.

2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?
O livro permanece, mas o campo atores fica vazio. Pode ser feito um signal pre-commit que valide isso.