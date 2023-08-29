# Matriz de Adjacência a partir de um Arquivo de Grafos

Este é um exemplo simples de código Python que demonstra como criar um grafo direcionado a partir de um arquivo de texto contendo arestas e, em seguida, gerar a matriz de adjacência desse grafo usando a biblioteca NetworkX e NumPy.

Como Usar

Crie um arquivo de texto chamado "grafo.txt" no formato abaixo:
1 2
2 3
3 1

Cada linha do arquivo representa uma aresta do grafo, com dois números inteiros separados por espaço indicando os vértices de origem e destino da aresta.

Execute o script main.py. Ele lerá o arquivo "grafo.txt", criará o grafo direcionado correspondente e gerará a matriz de adjacência.

A matriz de adjacência resultante será impressa na saída padrão.

Você também pode fazer alterações no grafo criado, como adicionar ou remover arestas, conforme necessário.

Exemplo de Saída
A saída do script incluirá a matriz de adjacência gerada a partir do arquivo "grafo.txt" e uma demonstração de como fazer alterações no grafo.

Licença
Este código é fornecido sob a licença MIT.


## Requisitos

- Python 3.x
- Biblioteca NetworkX
- Biblioteca NumPy

Você pode instalar as bibliotecas NetworkX e NumPy usando o pip:

```bash
pip install networkx numpy.
