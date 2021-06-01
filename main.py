class Graph:

    def __init__(self, wierzcholki):
        self.v = wierzcholki
        self.graph = []

    def dodaj_krawedz(self, u, v, w):
        self.graph.append([u, v, w])

    def wypisz(self, dist):
        print("Odległość wierzchołka od źródła")
        for i in range(self.v):
            print(i, dist[i])

    def BellmanFord(self, src):
        dist = [float("Inf")] * self.v
        dist[src] = 0
        for _ in range(self.v - 1):
            for u, v, w in self.graph:
                if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                    dist[v] = dist[u] + w
        for u, v, w in self.graph:
            if dist[u] != float("Inf") and dist[u] + w < dist[v]:
                print("Graf zawiera ujemny cykl")
                return
        self.wypisz(dist)

def main():
    graf = Graph(5) # dla druiego rowne 13
    matrix = []
    with open("plik2.txt", 'r') as reader:
        for line in reader.readlines():
            matrix.append((line.strip()[:-1]).split(', '))
    wagi = []
    print(matrix)
    g = open("wagi2.txt", "r")
    wagi = g.read()
    wagi = wagi.split(', ')
    k = 0
    for i,row in enumerate(matrix):
        for j in range(1, len(row)):
            graf.dodaj_krawedz(int(matrix[i][0]), int(row[j]), int(wagi[k]))
            k += 1
    graf.BellmanFord(0)
main()
