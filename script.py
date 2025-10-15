from collections import deque
import matplotlib.pyplot as plt
import networkx as nx

class Grafo:
    def __init__(self, arquivo):
        self.grafo = {}
        self.values = 0
        self.load_data(arquivo)

    def load_data(self, arquivo):
        with open(arquivo, 'r') as f:
            linhas = f.readlines()
            self.values = int(linhas[0].strip())
            for linha in linhas[1:]:  
                linha = linha.strip()
                if linha: 
                    a, b = map(int, linha.split())
                    self.add_edge(a, b)
            
    def add_edge(self, a, b):
        if a not in self.grafo:
            self.grafo[a] = []
        if b not in self.grafo:
            self.grafo[b] = []
        
        if b not in self.grafo[a]:
            self.grafo[a].append(b)
        if a not in self.grafo[b]:
            self.grafo[b].append(a)

    def calcular_numero_de_bacon(self, vertice_inicial, vertice_final):
        if vertice_inicial == vertice_final:
            return 0

        visitados = set()
        fila = deque([(vertice_inicial, [], 0)])

        while fila:
            vertice_atual, caminho, distancia = fila.popleft()
            visitados.add(vertice_atual)

            for vizinho in self.grafo.get(vertice_atual, []):
                if vizinho == vertice_final:
                    caminho_completo = caminho + [vertice_atual]
                    self.print_caminho(caminho_completo + [vizinho], vertice_final)
                    return distancia + 1
                if vizinho not in visitados:
                    visitados.add(vizinho)
                    fila.append((vizinho, caminho + [vertice_atual], distancia + 1))

        return -1

    def print_caminho(self, caminho, vertice_final):
        print("Caminho encontrado:", " -> ".join(map(str, caminho)))
        print(f"Chegou ao vértice final: {vertice_final}")

    def plotar_grafo(self):
        G = nx.Graph()
        for vertice, vizinhos in self.grafo.items():
            for vizinho in vizinhos:
                G.add_edge(vertice, vizinho)

        pos = nx.spring_layout(G)
        nx.draw(G, pos, with_labels=True, node_color='lightblue', node_size=500, font_size=16, font_weight='bold', edge_color='gray')
        plt.title('Representação do Grafo')
        plt.show()


caminho_arquivo = 'num.txt'  
grafh = Grafo(caminho_arquivo) 

vertice_inicial = grafh.values  
for vertice in grafh.grafo.keys():  
    if vertice != vertice_inicial:
        distancia = grafh.calcular_numero_de_bacon(vertice_inicial, int(vertice))
        if distancia != -1:
            print(f"Distância de {vertice_inicial} a {int(vertice)}: {distancia}\n")
        else:
            print(f"Não há caminho de {vertice_inicial} a {int(vertice)}.\n")


grafh.plotar_grafo()
