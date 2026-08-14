# Exercícios de Python

## 1. Fundamentos de Python

### 1.1 Tipos e estruturas de dados

Crie uma lista com **10 números inteiros**.

Escreva uma função que receba essa lista e retorne:

* O maior valor;
* O menor valor;
* A média dos valores.

---

### 1.2 Manipulação de strings

Escreva uma função que receba um **texto** e:

* Conte quantas vogais existem;
* Retorne o texto invertido;
* Verifique se o texto é um palíndromo.

---

### 1.3 Dicionários e compreensão de listas

Dada a lista:

```python
["Ana", "Bruno", "Carlos", "Ana", "Bruno", "Ana"]
```

Crie um dicionário que mostre **quantas vezes cada nome aparece**.

**Extra:** transforme a solução em uma **list comprehension** que retorne apenas os nomes que aparecem mais de uma vez.

---

# 2. POO em Python

## 2.1 Classe simples

Crie uma classe `Pessoa` com os seguintes atributos:

* `nome`
* `idade`
* `email`

Crie um método que exiba as informações da pessoa em formato de string.

Instancie pelo menos **3 objetos** e teste a classe.

---

## 2.2 Encapsulamento e validação

Na classe `Pessoa`, garanta que a **idade não pode ser negativa**.

Adicione também um método:

```python
aniversario()
```

Esse método deve aumentar a idade da pessoa em **1 ano**.

---

## 2.3 Herança

Crie uma classe `Aluno` que herde de `Pessoa`.

Adicione os seguintes atributos:

* `matricula`
* `curso`

Crie um método:

```python
exibir_dados_aluno()
```

Esse método deve mostrar **todas as informações do aluno**, incluindo os atributos herdados da classe `Pessoa`.

---

## 2.4 Composição

Crie uma classe `Curso` com os seguintes atributos:

* `nome`
* `alunos` — uma lista de objetos da classe `Aluno`.

Crie métodos para:

* Adicionar um aluno ao curso;
* Listar todos os alunos matriculados.

---

# 3. Mini-desafio

## Sistema de gerenciamento de cursos

Crie um **sistema simples de gerenciamento de cursos no terminal.**

O sistema deve permitir:

1. **Cadastrar cursos**;
2. **Adicionar alunos a um curso**;
3. **Liste os cursos e seus respectivos alunos**;