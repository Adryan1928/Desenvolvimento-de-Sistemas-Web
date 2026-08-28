const prompt = require('prompt-sync')({ sigint: true });

function main() {
    var q = 0;
    do {
        console.log("Escolha uma questão (1-17):");
        q = parseInt(prompt("Digite o número da questão: "));

        switch (q) {
            case 1:
                Q1();
                break;
            case 2:
                Q2();
                break;
            case 3:
                Q3();
                break;
            case 4:
                Q4();
                break;
            case 5:
                Q5();
                break;
            case 6:
                Q6();
                break;
            case 7:
                Q7();
                break;
            case 8:
                Q8();
                break;
            case 9:
                Q9();
                break;
            case 10:
                Q10();
                break;
            case 11:
                Q11();
                break;
            case 12:
                Q12();
                break;
            case 13:
                Q13();
                break;
            case 14:
                Q14();
                break;
            case 15:
                Q15();
                break;
            case 16:
                Q16();
                break;
            case 17:
                Q17();
                break;
            case 0:
                console.log("Saindo do programa.");
                break;
            default:
                console.log("Opção inválida. Por favor, escolha uma questão entre 1 e 17 ou digite 0 para sair.");
        }
    } while (q!=0);
}

function Q1() {
    segundos = parseInt(prompt("Digite a quantidade de segundos: "));

    time = new Date(segundos * 1000).toISOString()
    console.log("Tempo convertido: " + time.substr(11, 8));
}

function Q2() {
    celsius = parseFloat(prompt("Digite a temperatura em Celsius: "));

    farenheit = (celsius * 9/5) + 32;
    console.log("Temperatura em Farenheit: " + farenheit.toFixed(2));
    kelvin = celsius + 273.15;
    console.log("Temperatura em Kelvin: " + kelvin.toFixed(2));
}

function Q3() {
    price = parseFloat(prompt("Digite o preço do produto: "));
    qtd = parseInt(prompt("Digite a quantidade de produtos: "));

    total = price * qtd;

    if (total > 100) {
        total *= 0.95
    } else if (total > 300) {
        total *= 0.90
    }

    console.log(`Total da compra: ${total.toFixed(2)}`);
}

function Q4() {
    nascimento = parseInt(prompt("Digite o ano de nascimento: "));

    idade = 2026 - nascimento;
    console.log(`Idade: ${idade}`);

    if (idade < 16) {
        console.log("Não pode votar. Isento do serviço militar.");
    } else if (idade >= 16 && idade < 18) {
        console.log("Voto não obrigatório. Isento do serviço militar.");
    } else {
        console.log("Voto obrigatório. Obrigatório o serviço militar.");
    }
}

function Q5() {
    n1 = parseFloat(prompt("Digite o primeiro número: "));
    n2 = parseFloat(prompt("Digite o segundo número: "));
    op = prompt("Digite a operação (+, -, *, /): ");

    result = calc(n1, n2, op);

    if (result !== null) {
        console.log(`Resultado: ${result}`);
    }
}

function calc(n1, n2, op) {
    switch (op) {
        case '+':
            return n1 + n2;
        case '-':
            return n1 - n2;
        case '*':
            return n1 * n2;
        case '/':
            if (n2 === 0.0) {
                console.log("Erro: Divisão por zero.");
                return null;
            }
            return n1 / n2;
        default:
            console.log("Operação inválida.");
            return null;
    }
}

function Q6() {
    peso = parseFloat(prompt("Digite o peso da pessoa (em kg): "));
    altura = parseFloat(prompt("Digite a altura da pessoa (em metros): "));

    imc = peso / (altura * altura);
    console.log(`IMC: ${imc.toFixed(2)}`);

    if (imc < 18.5) {
        console.log("Abaixo do peso.");
    } else if (imc >= 18.5 && imc < 25) {
        console.log("Peso normal.");
    } else if (imc >= 25 && imc < 30) {
        console.log("Sobrepeso.");
    } else {
        console.log("Obesidade.");
    }
}

function Q7() {
    p1 = prompt("Escolha pedra, papel ou tesoura: ");
    p2 = prompt("Escolha pedra, papel ou tesoura: ");

    if (p1 === p2) {
        console.log("Empate!");
    } else if (
        (p1 === "pedra" && p2 === "tesoura") ||
        (p1 === "papel" && p2 === "pedra") ||
        (p1 === "tesoura" && p2 === "papel")
    ) {
        console.log("Jogador 1 vence!");
    } else {
        console.log("Jogador 2 vence!");
    }
}

function Q8() {
    num = prompt("Digite uma palavra: ");
    isPalin = isPalindrome(num);
    
    if (isPalin) {
        console.log("A palavra é um palíndromo.");
    } else {
        console.log("A palavra não é um palíndromo.");
    }
}

function isPalindrome(str) {
    const cleanedStr = str.toLowerCase().trim();
    const reversedStr = cleanedStr.split('').reverse().join('');
    return cleanedStr === reversedStr;
}

function Q9() {
    n = 0
    notas = []
    while (n >= 0) {
        n = parseInt(prompt("Digite uma nota (negativo para sair): "));
        if (n >= 0) {
            notas.push(n);
        }
    }
    media = notas.reduce((a, b) => a + b, 0) / notas.length;
    min = Math.min(...notas);
    max = Math.max(...notas);
    console.log(`Mínima: ${min}`);
    console.log(`Máxima: ${max}`);
    console.log(`Média: ${media.toFixed(2)}`);
}

function Q10() {
    n = parseInt(prompt("Digite um número: "));
    result = fibonacci(n);
    console.log(`Fibonacci(${n}): ${result}`);
}

function fibonacci(n) {
    if (n <= 1) {
        return n;
    }

    return fibonacci(n - 1) + fibonacci(n - 2);
}

function Q11() {
    password = prompt("Digite uma senha: ");
    validationMessage = validatePassword(password);
    console.log(validationMessage);
}

function validatePassword(password) {
    if (password.length < 8) {
        return "A senha deve ter pelo menos 8 caracteres.";
    } else if (!/[A-Z]/.test(password)) {
        return "A senha deve conter pelo menos uma letra maiúscula.";
    } else if (!/[0-9]/.test(password)) {
        return "A senha deve conter pelo menos um número.";
    } else {
        return "Senha válida.";
    }
}

function Q12() {
    estoque = [
        { nome: "Produto 1", quantidade: 10, preco: 5.0 },
        { nome: "Produto 2", quantidade: 20, preco: 10.0 },
        { nome: "Produto 3", quantidade: 30, preco: 15.0 }
    ]

    minimo = parseInt(prompt("Digite a quantidade mínima para alerta: "));
    analise = analiseEstoque(estoque, minimo);
    console.log(`Valor Total: ${analise.ValorTotal}; - Produto Mais Caro: ${analise.ProdutoMaisCaro.nome} - Preço: ${analise.ProdutoMaisCaro.preco}; - Produtos em Alerta: ${analise.ProdutosEmAlerta.map(p => p.nome).join(", ")}`);
}

function analiseEstoque(estoque, minimo) {
    let valorTotal = estoque.reduce((total, produto) => total + (produto.quantidade * produto.preco), 0);
    let produtoMaisCaro = estoque.find(produto => produto.preco === Math.max(...estoque.map(p => p.preco)));
    let produtosEmAlerta = estoque.filter(produto => produto.quantidade <= minimo);

    return {
        ValorTotal: valorTotal,
        ProdutoMaisCaro: produtoMaisCaro,
        ProdutosEmAlerta: produtosEmAlerta
    };
}

function Q13() {
    agenda = [
        { nome: "Contato 1", telefone: "123456789", categoria: "Amigos" },
        { nome: "Contato 2", telefone: "987654321", categoria: "Família" },
        { nome: "Contato 3", telefone: "456789123", categoria: "Trabalho" },
        { nome: "Contato 4", telefone: "123456239", categoria: "Amigos" }
    ];

    action = 0

    do {
        action = parseInt(prompt("Escolha uma ação: 1 - Adicionar contato, 2 - Remover contato, 3 - Listar contatos por categoria, 0 - Sair: "));

        switch (action) {
            case 1:
                nome = prompt("Digite o nome do contato: ");
                telefone = prompt("Digite o telefone do contato: ");
                categoria = prompt("Digite a categoria do contato: ");
                agenda.push({ nome, telefone, categoria });
                console.log("Contato adicionado.");
                break;
            case 2:
                nome = prompt("Digite o nome do contato a ser removido: ");
                index = agenda.findIndex(contato => contato.nome === nome);
                if (index !== -1) {
                    agenda.splice(index, 1);
                    console.log("Contato removido.");
                } else {
                    console.log("Contato não encontrado.");
                }
                break;
            case 3:
                categoria = prompt("Digite a categoria para listar os contatos: ");
                contatosFiltrados = agenda.filter(contato => contato.categoria === categoria);
                if (contatosFiltrados.length > 0) {
                    console.log(`Contatos na categoria ${categoria}:`);
                    contatosFiltrados.forEach(contato => {
                        console.log(`Nome: ${contato.nome}, Telefone: ${contato.telefone}`);
                    });
                } else {
                    console.log("Nenhum contato encontrado nessa categoria.");
                }
                break;
            case 0:
                console.log("Saindo do programa.");
                break;
            default:
                console.log("Opção inválida. Por favor, escolha uma ação válida.");
        }

    } while (action != 0);
}

class Produto {
    constructor(nome, preco, quantidade) {
        this.nome = nome;
        this.preco = preco;
        this.quantidade = quantidade;
    }

    aplicarDesconto(percentual) {
        this.preco -= this.preco * (percentual / 100);
    }

    produtoDisponivel() {
        return this.quantidade > 0;
    }
}

function Q14() {
    p1 = new Produto("Produto 1", 100, 10);
    p2 = new Produto("Produto 2", 200, 0);
    p3 = new Produto("Produto 3", 300, 5);

    console.log(`Nome: ${p1.nome}, Preço: ${p1.preco}, Quantidade: ${p1.quantidade}`);
    console.log(`Nome: ${p2.nome}, Preço: ${p2.preco}, Quantidade: ${p2.quantidade}`);
    console.log(`Nome: ${p3.nome}, Preço: ${p3.preco}, Quantidade: ${p3.quantidade}`);

    p1.aplicarDesconto(10);
    console.log(`Preço após desconto: ${p1.preco}`);
    console.log(`Produto 1 disponível: ${p1.produtoDisponivel()}`);
    console.log(`Produto 2 disponível: ${p2.produtoDisponivel()}`);
}

class ContaBancaria {
    constructor(titular, saldo) {
        this.titular = titular;
        this.saldo = saldo;
    }

    depositar(valor) {
        if (valor > 0) {
            this.saldo += valor;
            console.log(`Depósito de ${valor} realizado. Novo saldo: ${this.saldo}`);
        } else {
            console.log("Valor de depósito inválido.");
        }
    }
    
    sacar(valor) {
        if (valor > 0 && valor <= this.saldo) {
            this.saldo -= valor;
            console.log(`Saque de ${valor} realizado. Novo saldo: ${this.saldo}`);
        } else {
            console.log("Valor de saque inválido.");
        }
    }

    extrato() {
        return `Titular: ${this.titular}, Saldo: ${this.saldo}`
    }
}

function Q15() {
    conta1 = new ContaBancaria("João", 1000);
    console.log(conta1.extrato());
    conta1.depositar(500);
    conta1.sacar(200);
    console.log(conta1.extrato());

    conta2 = new ContaBancaria("Maria", 2000);
    console.log(conta2.extrato());
    conta2.depositar(1000);
    conta2.sacar(500);
    console.log(conta2.extrato());
}

class Retangulo {
    constructor(base, altura) {
        this.base = base;
        this.altura = altura;
    }

    calcularArea() {
        return this.base * this.altura;
    }

    calcularPerimetro() {
        return 2 * (this.base + this.altura);
    }
}

function Q16() {
    r1 = new Retangulo(5, 10);
    console.log(`Área: ${r1.calcularArea()}`);
    console.log(`Perímetro: ${r1.calcularPerimetro()}`);
}

class Contato {
    constructor(nome, telefone, categoria) {
        this.nome = nome;
        this.telefone = telefone;
        this.categoria = categoria;
    }
}

class Agenda {
    constructor() {
        this.contatos = [];
    }

    adicionarContato(contato) {
        this.contatos.push(contato);
    }

    removerContato(nome) {
        let index = this.contatos.findIndex(contato => contato.nome === nome);
        if (index !== -1) {
            this.contatos.splice(index, 1);
            console.log("Contato removido.");
        } else {
            console.log("Contato não encontrado.");
        }
    }

    listarContatosPorCategoria(categoria) {
        let contatosFiltrados = this.contatos.filter(contato => contato.categoria === categoria);
        if (contatosFiltrados.length > 0) {
            console.log(`Contatos na categoria ${categoria}:`);
            contatosFiltrados.forEach(contato => {
                console.log(`Nome: ${contato.nome}, Telefone: ${contato.telefone}`);
            });
        } else {
            console.log("Nenhum contato encontrado nessa categoria.");
        }
    }
}

// Esse é mais organizado
function Q17() {
    c1 = new Contato("Contato 1", "123456789", "Amigos");
    c2 = new Contato("Contato 2", "987654321", "Família");
    c3 = new Contato("Contato 3", "456789123", "Trabalho");

    agenda = new Agenda();
    agenda.adicionarContato(c1);
    agenda.adicionarContato(c2);
    agenda.adicionarContato(c3);

    agenda.listarContatosPorCategoria("Amigos");
    agenda.removerContato("Contato 1");
    agenda.listarContatosPorCategoria("Amigos");
}

main()