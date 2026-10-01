# Sistema de Controle de Produção e Qualidade

## Sobre o projeto

Este projeto consiste em um protótipo desenvolvido em Python para auxiliar no controle de produção e na inspeção de qualidade de peças fabricadas em uma linha de montagem.

O sistema recebe os dados de cada peça e verifica automaticamente se ela atende aos critérios de qualidade definidos.

### Critérios de aprovação

Uma peça é considerada aprovada quando atende simultaneamente aos seguintes critérios:

* Peso entre 95g e 105g;
* Cor azul ou verde;
* Comprimento entre 10cm e 20cm.

Caso algum critério não seja atendido, a peça é classificada como reprovada e o sistema informa o motivo da reprovação.

## Funcionalidades

O sistema possui um menu interativo com as seguintes opções:

1. Cadastrar nova peça
2. Listar peças aprovadas/reprovadas
3. Remover peça cadastrada
4. Listar caixas fechadas
5. Gerar relatório final
6. Sair

### Cadastro de peças

Para cadastrar uma peça, o usuário informa:

* ID;
* Peso;
* Cor;
* Comprimento.

O sistema realiza automaticamente a avaliação da peça.

### Controle de caixas

As peças aprovadas são adicionadas a uma caixa.

Cada caixa possui capacidade máxima de 10 peças.

Quando uma caixa atinge 10 peças, ela é fechada automaticamente e uma nova caixa começa a ser preenchida.

### Relatório

O relatório final apresenta:

* Total de peças cadastradas;
* Total de peças aprovadas;
* Total de peças reprovadas;
* Motivos das reprovações;
* Quantidade de caixas fechadas;
* Quantidade de peças presentes na caixa atual.

## Tecnologias utilizadas

* Python 3
* Estruturas condicionais
* Estruturas de repetição
* Funções
* Listas
* Dicionários

Não são necessárias bibliotecas externas para executar o projeto.

## Como executar o programa

### 1. Instalar o Python

Instale o Python 3 no computador caso ele ainda não esteja instalado.

### 2. Baixar o projeto

Baixe ou clone este repositório do GitHub.

### 3. Abrir a pasta do projeto

Abra o terminal ou prompt de comando dentro da pasta onde está o arquivo Python.

### 4. Executar o programa

No terminal, execute:

```bash
python sistema.py
```

Caso o computador utilize o comando `python3`, execute:

```bash
python3 sistema.py
```

### 5. Utilizar o menu

Após executar o programa, o menu principal será apresentado:

```text
================================
 SISTEMA DE CONTROLE INDUSTRIAL
================================

1 - Cadastrar nova peça
2 - Listar peças aprovadas/reprovadas
3 - Remover peça cadastrada
4 - Listar caixas fechadas
5 - Gerar relatório final
0 - Sair
```

Digite o número correspondente à operação desejada.

## Exemplo de entrada

### Cadastro de uma peça aprovada

```text
Escolha uma opção: 1

===== CADASTRAR NOVA PEÇA =====

Digite o ID da peça: 1
Digite o peso da peça (g): 100
Digite a cor da peça: azul
Digite o comprimento da peça (cm): 15
```

### Saída

```text
PEÇA APROVADA
Peça adicionada à caixa atual.
```

## Exemplo de peça reprovada

### Entrada

```text
Escolha uma opção: 1

===== CADASTRAR NOVA PEÇA =====

Digite o ID da peça: 2
Digite o peso da peça (g): 110
Digite a cor da peça: azul
Digite o comprimento da peça (cm): 15
```

### Saída

```text
PEÇA REPROVADA

Motivos:
- Peso fora do padrão
```

## Exemplo de listagem

Após cadastrar algumas peças, o usuário pode escolher:

```text
Escolha uma opção: 2
```

O sistema apresentará informações semelhantes a:

```text
===== LISTA DE PEÇAS =====

ID: 1
Peso: 100.0 g
Cor: azul
Comprimento: 15.0 cm
Status: Aprovada

ID: 2
Peso: 110.0 g
Cor: azul
Comprimento: 15.0 cm
Status: Reprovada
Motivos:
- Peso fora do padrão
```

## Exemplo de caixas

Após cadastrar 10 peças aprovadas:

```text
===== CAIXAS FECHADAS =====

Caixa 1
Quantidade de peças: 10
IDs das peças: [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
```

## Exemplo de relatório

```text
========== RELATÓRIO FINAL ==========

Total de peças cadastradas: 12
Total de peças aprovadas: 10
Total de peças reprovadas: 2

Motivos das reprovações:
- Peso fora do padrão: 1
- Cor inválida: 1

Caixas fechadas: 1
Não há caixa em aberto.

======================================
```

## Estrutura do projeto

```text
sistema-controle-industrial/
│
├── sistema.py
└── README.md
```

## Objetivo acadêmico

O projeto tem como objetivo demonstrar a aplicação de conceitos fundamentais de programação em Python na construção de um protótipo de automação para controle de produção e qualidade.

A solução utiliza decisões, funções, condições, repetições, listas e dicionários para representar o processo de inspeção e organização das peças.

## Possíveis expansões

Em uma aplicação real, o sistema poderia ser expandido para utilizar:

* Sensores industriais;
* Sistemas de banco de dados;
* Visão computacional;
* Inteligência artificial;
* Integração com equipamentos da linha de produção;
* Sistemas de gestão industrial;
* Painéis para acompanhamento dos indicadores.
