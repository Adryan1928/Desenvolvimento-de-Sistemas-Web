# models.CASCADE - Justificativa de escolha:
Quando alguém tentar apagar um autor que tem livros, os livros precisam ser apagados também. Essa associação faz sentido porque os livros obrigatoriamente precisam de um autor.


1. Que dados se perdem quando a migração é revertida? Por quê?
Nenhum dado é perdido por causa da reverse_autor_to_atores.

2. Com ManyToMany, o que acontece com um livro quando o seu único autor é apagado? Como garantir que todo livro tenha pelo menos um autor?
O livro permanece, mas o campo atores fica vazio. Pode ser feito um signal pre-commit que valide isso.


## Atividade - Biblioteca: Formulários - parte 1

1. Teste e anote no README o que acontece quando essa proteção é removida do template.

Ao remover a proteção, que é o csrf_token, o Django não permite que o formulário seja enviado. Ele retorna um erro 403 (Forbidden) e não processa os dados do formulário.

Erro identificado:
Forbidden (403)
CSRF verification failed. Request aborted.


## Atividade Sábado Letivo 1 -  validators, upload e CBV

- 1.2
    - A: Sim, porque no meu caso não estou usando o '__all__' nos fields, então preciso modificar isso manualmente junto com os labels. Por ser um model form, ele já consegue identificar essas modificações na model e refletir isso no admin e no próprio template, chamando o form ou usando um for para passar por cada campo.

    - B: Validator apenas valida o valor e retorna um true ou false para o formulário indicanto o erro, além de ele ser aplicado na model para poder ser reutilizado. O clean é aplicado no formulário como um processo de sanitização, onde se é necessário fazer uma validação, mas também aplicar métodos como strip ou lowerCase. Exemplo disso seria um campo de email, onde ele não é case sensitive, ou seja, pode-se aplicar um clean com o lower case para idependente da entrada do usuário, sempre lidar com ele em letras minúsculas.

    - C: 
        - O título não pode ser igual ao nome do autor.
            Validator, porque não podemos modificar por conta própria, então deve-se retorna o erro ao usuário e pedir uma nova entrada.
        - O título deve ser salvo sem espaços no início e no fim.
            clean_<campo\>, porque podemos fazer esse processo de sanitização sem intervenção do usuário, e por ser em um único campo, basta usar o clean_<campo\> 
        - O número de páginas deve ser no máximo 5000.
            Validator, porque não podemos modificar por conta própria, então deve-se retorna o erro ao usuário e pedir uma nova entrada.
        - Um livro "indisponível" precisa ter o ISBN preenchido.
            clean, porque envolve mais de um campo e é uma validação no formulário.

- 2.2
    - A: Sem passar `request.FILES` ao formulário, o arquivo que chegou ao servidor não é associado ao campo. Sem `enctype="multipart/form-data"`, o navegador não envia o conteúdo do arquivo como upload e `request.FILES` fica vazio. Em nenhum do casos dá erro, mas em nenhum a imagem é modificada, ou seja, o forms não retornar nenhum erro, mas não acontece o comportamento esperado.

    - B: Arquivos estáticos são recursos da aplicação distribuídos junto com o código, como CSS, JavaScript e ícones; `STATICFILES_DIRS` informa diretórios adicionais de busca e `{% static '...' %}` gera sua URL. `MEDIA_ROOT` é o diretório de armazenamento dos arquivos enviados pelos usuários; o campo `ImageField` guarda o caminho relativo e `livro.capa.url` fornece a URL para exibi-lo. Na Mini biblioteca, estilos e ícones pertencem a static; capas cadastradas pertencem a media.

    - C: O banco guarda apenas o caminho do arquivo. Excluir o registro ou substituir esse caminho não apaga automaticamente o arquivo do armazenamento. Com o tempo, capas órfãs ocupam espaço, aumentam o custo de armazenamento e backups e podem permanecer acessíveis sem estarem associadas a um livro.

    - D: A extensão é apenas parte do nome e pode ser falsificada; um arquivo com sufixo `.png` não necessariamente contém uma imagem PNG segura. `ImageField` valida o conteúdo da imagem, mas isso não substitui controles de segurança. O servidor também deve impor limites de tamanho e, conforme o risco, dimensões e quantidade de pixels; não confiar no nome nem no MIME type informado pelo cliente; gerar nomes seguros; armazenar uploads sem permissão de execução e, quando possível, fora da raiz pública; restringir quem pode enviar arquivos;
