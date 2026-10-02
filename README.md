# Programação Orientada a Objetos em Python

Exercícios e pequenos sistemas que desenvolvi em 2026 estudando Programação Orientada a Objetos, durante o curso de Ciência da Computação no IFC (Instituto Federal Catarinense).

As pastas estão numeradas na ordem em que os conteúdos foram estudados, do primeiro `class` até polimorfismo com classes abstratas.

## Conteúdo

| Pasta | Conceitos | O que tem |
| --- | --- | --- |
| [`01_classes`](01_classes) | Classes, atributos, métodos, `__init__`, `__str__` | Classes independentes: calculadora, aluno com média, retângulo, produto em estoque, filme, restaurante |
| [`02_importacao_reutilizacao`](02_importacao_reutilizacao) | Módulos, `import`, atributo de classe, `@staticmethod` | Biblioteca de livros com empréstimo e consulta de disponibilidade |
| [`03_heranca`](03_heranca) | Herança, `super()`, sobrescrita de `__str__` | Carros e motos que herdam de uma classe `Veiculo` |
| [`04_polimorfismo_metodo_abstrato`](04_polimorfismo_metodo_abstrato) | Classes abstratas (`ABC`), `@abstractmethod`, polimorfismo | Cinco sistemas, descritos abaixo |

### Sistemas da pasta 04

| Sistema | Descrição |
| --- | --- |
| [`sistema_pagamentos`](04_polimorfismo_metodo_abstrato/sistema_pagamentos) | Pagamento por cartão de crédito, boleto e Pix, cada um com sua própria regra de taxa |
| [`sistema_funcionarios`](04_polimorfismo_metodo_abstrato/sistema_funcionarios) | Cálculo de salário de gerente (bônus fixo) e programador (hora extra) |
| [`calculadora_area`](04_polimorfismo_metodo_abstrato/calculadora_area) | Área de formas geométricas a partir de uma classe `Forma` abstrata |
| [`sistema_pessoas`](04_polimorfismo_metodo_abstrato/sistema_pessoas) | Aluno e professor com apresentações diferentes |
| [`veiculos`](04_polimorfismo_metodo_abstrato/veiculos) | Classe `Veiculo` abstrata com o método `ligar` |

## Como executar

É preciso ter o Python 3 instalado. Não há dependências externas.

```bash
git clone https://github.com/JuuCarmona/POO.git
cd POO
```

Os arquivos da pasta `01_classes` rodam sozinhos:

```bash
python 01_classes/retangulo.py
```

Nas outras pastas, cada sistema tem um `main.py`. Entre na pasta do sistema antes de rodar, para que os imports funcionem:

```bash
cd 04_polimorfismo_metodo_abstrato/sistema_pagamentos
python main.py
```

Saída desse exemplo:

```text
PAGAMENTO CARTÃO DE CRÉDITO
Valor original:R$100
Número do cartão:12345
Valor com taxa: R$110.0
------------------------------
PAGAMENTO BOLETO
Valor original:R$200
Gerando boleto para Maria da Silva
CPF:000.000.000-00
Valor final:R$203.0
------------------------------
PAGAMENTO PIX
valor original:R$150
chave pix:maria@exemplo.com
------------------------------
```

## Autora

Julia Carmona, estudante de Ciência da Computação no IFC.
[github.com/JuuCarmona](https://github.com/JuuCarmona)
