# Trabalho 04 - Grafos: Algoritmo de Busca e Visualização

[![Python](https://img.shields.io/badge/python-3.7+-blue.svg)](https://www.python.org/downloads/)
[![NetworkX](https://img.shields.io/badge/NetworkX-3.0+-green.svg)](https://networkx.org/)
[![Matplotlib](https://img.shields.io/badge/Matplotlib-3.0+-orange.svg)](https://matplotlib.org/)

Este projeto implementa um algoritmo de busca em grafos não-direcionados, calculando a menor distância entre vértices usando o conceito similar ao "Número de Bacon". O projeto inclui visualização gráfica do grafo e análise de conectividade.

## Funcionalidades

- **Carregamento de Grafos**: Leitura de dados de grafo a partir de arquivo de texto
- **Busca em Largura (BFS)**: Implementação de algoritmo BFS para encontrar menor caminho
- **Cálculo de Distâncias**: Determinação da menor distância entre qualquer par de vértices
- **Visualização**: Representação gráfica do grafo usando NetworkX e Matplotlib
- **Análise de Conectividade**: Verificação se existe caminho entre vértices

## Estrutura do Projeto

```
trabalho04-grafos/
├── script.py      # Implementação principal da classe Grafo
├── num.txt        # Arquivo de entrada com dados do grafo
└── README.md      # Documentação do projeto
```

## Como Usar

### Pré-requisitos

Instale as dependências necessárias:

```bash
pip install matplotlib networkx
```

### Executando o Programa

1. **Execute o script principal**:
   ```bash
   python script.py
   ```

2. **O programa irá**:
   - Carregar o grafo do arquivo `num.txt`
   - Calcular as distâncias entre o vértice inicial e todos os outros vértices
   - Exibir os caminhos encontrados
   - Mostrar uma visualização gráfica do grafo

### Formato do Arquivo de Entrada

O arquivo `num.txt` deve seguir o formato:

```
n
v1 v2
v3 v4
...
```

Onde:
- `n` é o número do vértice inicial (primeira linha)
- Cada linha subsequente representa uma aresta entre dois vértices

**Exemplo** (`num.txt`):
```
5
1 2
2 5
5 3
4 5
1 5
```

Este exemplo cria um grafo com vértice inicial 5 e as seguintes arestas:
- 1 ↔ 2
- 2 ↔ 5  
- 5 ↔ 3
- 4 ↔ 5
- 1 ↔ 5

## Implementação

### Classe Grafo

A classe principal `Grafo` oferece os seguintes métodos:

- `__init__(arquivo)`: Inicializa o grafo carregando dados do arquivo
- `load_data(arquivo)`: Carrega dados do arquivo de entrada
- `add_edge(a, b)`: Adiciona uma aresta não-direcionada entre vértices
- `calcular_numero_de_bacon(inicial, final)`: Calcula menor distância usando BFS
- `print_caminho(caminho, final)`: Exibe o caminho encontrado
- `plotar_grafo()`: Visualiza o grafo graficamente

### Algoritmo de Busca

O algoritmo implementado é uma **Busca em Largura (BFS)** que:

1. Utiliza uma fila para explorar vértices nivel por nivel
2. Mantém controle de vértices visitados
3. Retorna a menor distância entre dois vértices
4. Reconstrói e exibe o caminho encontrado

## Exemplo de Saída

```
Caminho encontrado: 5 -> 1
Chegou ao vértice final: 1
Distância de 5 a 1: 1

Caminho encontrado: 5 -> 2
Chegou ao vértice final: 2
Distância de 5 a 2: 1

Caminho encontrado: 5 -> 3
Chegou ao vértice final: 3
Distância de 5 a 3: 1

Caminho encontrado: 5 -> 4
Chegou ao vértice final: 4
Distância de 5 a 4: 1
```

## Visualização

O programa gera uma representação visual do grafo mostrando:
- Vértices como círculos azuis
- Arestas como linhas cinzas
- Rótulos dos vértices
- Layout automático usando algoritmo spring

## Conceitos Utilizados

- **Teoria dos Grafos**: Representação e manipulação de grafos não-direcionados
- **Busca em Largura (BFS)**: Algoritmo de busca para encontrar menor caminho
- **Número de Bacon**: Conceito de graus de separação entre elementos
- **Visualização de Dados**: Representação gráfica de estruturas de dados

## Tecnologias

- **Python 3.7+**: Linguagem de programação principal
- **NetworkX**: Biblioteca para criação e análise de grafos
- **Matplotlib**: Biblioteca para visualização de dados
- **Collections.deque**: Estrutura de dados eficiente para BFS

## Complexidade

- **Tempo**: O(V + E) onde V é o número de vértices e E é o número de arestas
- **Espaço**: O(V) para armazenar vértices visitados e fila de busca

---
