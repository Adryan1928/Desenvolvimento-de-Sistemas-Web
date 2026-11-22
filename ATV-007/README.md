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

- 3.1
    - A: As funções já presentes na própria CBV já validam isso e chamam os métodos GET e POST: GET exibe o formulário; POST o valida e chama `form_valid` ou `form_invalid`. Se estiver inválido, a mesma página é renderizada novamente com os dados enviados e os erros de validação.

    - B: Porque já inclui `request.POST` e `request.FILES` automaticamente quando a requisição é POST. Assim, `CreateView` e `UpdateView` entregam os arquivos ao `ModelForm` automaticamente.

    - C: O GET é usado para exibir a confirmação; o POST expressa a ação de exclusão. Isso respeita a semântica HTTP de que GET não deve alterar dados. Excluir em GET permitiria que um link ou uma requisição indevida apagasse registros sem confirmação e poderia causar exclusões acidentais.

    - D: Uma vantagem é reutilizar comportamentos prontos (por exemplo, validação, renderização e redirecionamento de formulários) com menos código repetido. Uma desvantagem é que o fluxo pode ficar menos explícito e mais difícil de acompanhar quando envolve muitas mixins e sobrescritas. Eu escolheria uma FBV para um fluxo pequeno, específico ou com ramificações simples, quando a sequência explícita de passos for mais clara do que adaptar uma CBV genérica.


## Atividade Sábado Letivo 2 - Conexão com banco de dados

1. 
O SQLite é melhor para aplicações de pequeno porte, como teste locais e desenvolvimento, já que possui escalabilidade limitada.
O PostgreSQL é melhor para aplicações robusta, pois possui capacidade de escalabilidade e tem mais ferramentas, o tornando mais completo.

2. 
psycopg[binary]
pip install "psycopg[binary]" 

3. 
ENGINE: Backend usado pelo Django; aqui, `django.db.backends.postgresql`.
NAME: Nome do banco de dados no servidor PostgreSQL. No SQLite, seria o caminho do arquivo.
USER: Usuário do PostgreSQL usado pela aplicação na conexão.
PASSWORD: Senha desse usuário.
HOST: Endereço do servidor do banco; `localhost` nesta instalação local.
PORT: Porta TCP do serviço PostgreSQL; normalmente `5432`.

4. 
https://www.postgresql.org/docs/current/sql-createrole.html
```sql
CREATE ROLE biblioteca_app LOGIN NOSUPERUSER NOCREATEDB NOCREATEROLE
    NOINHERIT NOREPLICATION NOBYPASSRLS PASSWORD '<senha-forte>';
CREATE DATABASE biblioteca_db OWNER biblioteca_app;
\c biblioteca_db
GRANT USAGE, CREATE ON SCHEMA public TO biblioteca_app;
```

5. 
São variáveis que são lidas ao executar o código e não ficam salvas dentro dele. Isso garante uma maior segurança, já que senhas e keys secretas não ficam expostas no código e podem ser modificadas facilmente para cada ambiente.

6. 

Pode-se usar a biblioteca OS com a dotenv.

from dotenv import load_dotenv
load_dotenv()

os.getenv().

7. 
O .gitignore diz ao git quais pastas/arquivos ignorar durante um commit, para evitar que esses arquivos vão para o repositório.

Já o .env.exemple é somente um exemplo de um .env para ser copiado e depois mudar os valores para casos reais.

8. 

Todas as configurações de banco, o debug, allowed hosts, secret key, configurações de email...

Todas essas informações sensiveis e que tenham grande impacto no sistemas devem ficar no .env.

### Fontes
https://docs.djangoproject.com/en/6.1/ref/databases/#postgresql-notes
https://www.datacamp.com/pt/blog/sqlite-vs-postgresql-detailed-comparison
https://www.geeksforgeeks.org/python/python-os-getenv-method/
https://www.postgresql.org/docs/current/sql-createrole.html
https://docs.djangoproject.com/en/6.1/topics/db/fixtures/


### Evidências
![img](<test.png>)

### Settings

https://github.com/Adryan1928/Desenvolvimento-de-Sistemas-Web/blob/9950af59fd3dc52dbfbbae3fe00acd74aa921757/ATV-007/core/settings.py

https://github.com/Adryan1928/Desenvolvimento-de-Sistemas-Web/blob/81b494694504640ef86160483df0bc12fa18a5ad/ATV-007/core/settings.py