class Pessoa:
    def __init__(self, nome, idade, email):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return self.nome

    def apresentation(self):
        return f"Olá, meu nome é {self.nome}, tenho {self.idade} anos e meu email é {self.email}."

    def birthday(self):
        self.idade += 1
        return self.idade

try:
    pessoa1 = Pessoa("João", -10, "joao@example.com")
    print(pessoa1.apresentation())
    
except ValueError as e:
    print(e)

pessoa2 = Pessoa("Maria", 30, "maria@example.com")
print(pessoa2.apresentation())
pessoa3 = Pessoa("Carlos", 28, "carlos@example.com")
print(pessoa3.apresentation())

print(pessoa3.birthday())


class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.curso = None

    def exibir_dados_alunos(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}, Matrícula: {self.matricula}, Curso: {self.curso}"

Aluno1 = Aluno("Ana", 20, "ana@example.com", "12345")
Aluno2 = Aluno("Bruno", 22, "bruno@example.com", "67890")

print(Aluno1.exibir_dados_alunos())
print(Aluno2.exibir_dados_alunos())

class Curso:
    def __init__(self, nome):
        self.nome = nome
        self.alunos = []

    def adicionar_aluno(self, aluno:Aluno):
        if isinstance(aluno, Aluno):
            self.alunos.append(aluno)
            aluno.curso = self.nome
        else:
            raise ValueError("O objeto fornecido não é um aluno válido.")

    def listar_alunos(self):
        return [self.alunos[i].exibir_dados_alunos() for i in range(len(self.alunos))]

curso = Curso("Desenvolvimento de Sistemas Web")
curso.adicionar_aluno(Aluno1)
curso.adicionar_aluno(Aluno2)

print(curso.listar_alunos())

