class Pessoa:
    def __init__(self, nome, idade, email):
        if idade < 0:
            raise ValueError("A idade não pode ser negativa.")
        self.nome = nome
        self.idade = idade
        self.email = email

    def __str__(self):
        return self.nome

class Aluno(Pessoa):
    def __init__(self, nome, idade, email, matricula):
        super().__init__(nome, idade, email)
        self.matricula = matricula
        self.curso = None

    def exibir_dados_alunos(self):
        return f"Nome: {self.nome}, Idade: {self.idade}, Email: {self.email}, Matrícula: {self.matricula}, Curso: {self.curso}"


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


q = 1
cursos = []
alunos = []

while q != 0:
    print("Menu:")
    print("1. Adicionar Curso")
    print("2. Adicionar Aluno")
    print("3. Adicionar Aluno a um Curso")
    print("4. Listar Alunos")
    print("0. Sair")
    q = int(input("Escolha uma opção: "))

    match q:
        case 1:
            nome_curso = input("Digite o nome do curso: ")
            curso = Curso(nome_curso)
            cursos.append(curso)
            print(f"Curso '{nome_curso}' adicionado com sucesso!")
        case 2:
            nome = input("Digite o nome do aluno: ")
            idade = int(input("Digite a idade do aluno: "))
            email = input("Digite o email do aluno: ")
            matricula = input("Digite a matrícula do aluno: ")
            aluno = Aluno(nome, idade, email, matricula)
            alunos.append(aluno)
            print(f"Aluno {nome} adicionado com sucesso!")
        case 3:
            if not cursos:
                print("Nenhum curso disponível. Adicione um curso primeiro.")
                continue
            if not alunos:
                print("Nenhum aluno disponível. Adicione um aluno primeiro.")
                continue

            print("Cursos disponíveis:")
            for i, curso in enumerate(cursos):
                print(f"{i + 1}. {curso.nome}")

            curso_index = int(input("Escolha o número do curso: ")) - 1
            if curso_index < 0 or curso_index >= len(cursos):
                print("Curso inválido.")
                continue

            print("Alunos disponíveis:")
            for i, aluno in enumerate(alunos):
                print(f"{i + 1}. {aluno.nome}")

            aluno_index = int(input("Escolha o número do aluno: ")) - 1
            if aluno_index < 0 or aluno_index >= len(alunos):
                print("Aluno inválido.")
                continue

            cursos[curso_index].adicionar_aluno(alunos[aluno_index])
            print(f"Aluno {alunos[aluno_index].nome} adicionado ao curso {cursos[curso_index].nome} com sucesso!")
        case 4:
            if not cursos:
                print("Nenhum curso disponível. Adicione um curso primeiro.")
                continue
            print("Cursos disponíveis:")
            for i, curso in enumerate(cursos):
                print(f"{i + 1}. {curso.nome}")

            curso_index = int(input("Escolha o número do curso para listar os alunos: ")) - 1
            if curso_index < 0 or curso_index >= len(cursos):
                print("Curso inválido.")
                continue
            alunos_curso = cursos[curso_index].listar_alunos()
            if not alunos_curso:
                print(f"Nenhum aluno matriculado no curso {cursos[curso_index].nome}.")
            else:
                print(f"Alunos matriculados no curso {cursos[curso_index].nome}:")
                for aluno_info in alunos_curso:
                    print(aluno_info)
        case 0:
            print("Saindo do programa.")
        case _:
            print("Opção inválida. Tente novamente.")