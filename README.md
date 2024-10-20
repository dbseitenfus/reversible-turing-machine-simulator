# Reversible Turing Machine Simulator

Este projeto é um simulador de uma Máquina de Turing Reversível. Ele executa simulações de autômatos baseados em quíntuplas, que são convertidos em quádruplas para garantir reversibilidade lógica, permitindo a execução de cálculos de forma reversível, sem perda de informações.

Funcionalidades
- Simulação de Máquina de Turing Reversível: A máquina executa operações utilizando quíntuplas que são transformadas em quádruplas reversíveis.
- Fitas de Entrada, Histórico e Saída: O simulador utiliza três fitas — uma para a entrada de dados, uma para armazenar o histórico das operações e uma para a saída.
- Conversão de Quíntuplas para Quádruplas: O simulador automaticamente converte quíntuplas em quádruplas, separando as operações de leitura/escrita e movimento, garantindo a reversibilidade do cálculo.

## Estrutura do Projeto
O projeto é composto pelos seguintes componentes principais:

- `main.py`: O arquivo principal que contém as classes e a lógica para simular a máquina de Turing reversível.
Quintuple: Classe que representa uma quíntupla na forma (estado atual, símbolo lido) = (próximo estado, símbolo escrito, movimento).
- `Quadruple`: Classe que representa uma quádrupla utilizada na simulação reversível.
- `Tape`: Classe que representa uma fita, usada para armazenar símbolos durante a simulação.
- `Simulation`: Classe principal que executa a simulação da máquina de Turing reversível, incluindo a conversão de quíntuplas em quádruplas e a execução do cálculo em três estágios.

## Como Funciona
A simulação é dividida em três estágios:

- Cálculo Direto com Registro de Histórico: A máquina executa operações baseadas em quíntuplas fornecidas e armazena o histórico de cada operação na fita de histórico.
- Cópia da Saída: O resultado é copiado da fita de entrada para a fita de saída de forma reversível.
- Cálculo Reverso e Apagamento do Histórico: A máquina desfaz as operações realizadas, apagando o histórico e restaurando o estado original, preservando apenas a saída final.

## entrada-quintupla.txt

A primeira linha apresenta números, que indicam: 
- número de estados, 
- número de símbolos no alfabeto de entrada, 
- número de símbolos no alfabeto da fita 
- e número de transições, respectivamente. 

A seguir, temos:
- os estados, 
- alfabeto de entrada e
- alfabeto da fita 

Nas linhas sequentes temos:
- a funcão de transição (como explicada no artigo). 

Depois da funcão de transição, segue uma entrada. 

*** Lembrando que o estado de aceitação é o último, no caso do exemplo, o 6.