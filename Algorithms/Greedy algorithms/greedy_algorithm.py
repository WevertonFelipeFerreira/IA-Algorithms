from typing import Dict


def find_key_by_value(dictionary, value):
    for key, val in dictionary.items():
        if val == value:
            return key
    return None


class Vertex:
    def __init__(self, title):
        self.title = title
        self.visited = False
        self.adjacents = []

    def add_adjacent(self, adjacent):
        self.adjacents.append(adjacent)

    def show_adjascents(self):
        for i in self.adjacents:
            print(i.vertex.title, i.cust)


class Adjacent:
    def __init__(self, vertex, cust):
        self.vertex = vertex
        self.cust = cust


class Graph:
    arad = Vertex('Arad')
    zerind = Vertex('Zerind')
    oradea = Vertex('Oradea')
    sibiu = Vertex('Sibiu')
    timisoara = Vertex('Timisoara')
    lugoj = Vertex('Lugoj')
    mehadia = Vertex('Mehadia')
    dobreta = Vertex('Dobreta')
    craiova = Vertex('Craiova')
    rimnicu = Vertex('Rimnicu')
    fagaras = Vertex('Fagaras')
    pitesti = Vertex('Pitesti')
    bucharest = Vertex('Bucharest')
    giurgiu = Vertex('Giurgiu')

    arad.add_adjacent(Adjacent(zerind, 75))
    arad.add_adjacent(Adjacent(sibiu, 140))
    arad.add_adjacent(Adjacent(timisoara, 118))

    zerind.add_adjacent(Adjacent(arad, 75))
    zerind.add_adjacent(Adjacent(oradea, 71))

    oradea.add_adjacent(Adjacent(zerind, 71))
    oradea.add_adjacent(Adjacent(sibiu, 151))

    sibiu.add_adjacent(Adjacent(oradea, 151))
    sibiu.add_adjacent(Adjacent(arad, 140))
    sibiu.add_adjacent(Adjacent(fagaras, 99))
    sibiu.add_adjacent(Adjacent(rimnicu, 80))

    timisoara.add_adjacent(Adjacent(arad, 118))
    timisoara.add_adjacent(Adjacent(lugoj, 111))

    lugoj.add_adjacent(Adjacent(timisoara, 111))
    lugoj.add_adjacent(Adjacent(mehadia, 70))

    mehadia.add_adjacent(Adjacent(lugoj, 70))
    mehadia.add_adjacent(Adjacent(dobreta, 75))

    dobreta.add_adjacent(Adjacent(mehadia, 75))
    dobreta.add_adjacent(Adjacent(craiova, 120))

    craiova.add_adjacent(Adjacent(dobreta, 120))
    craiova.add_adjacent(Adjacent(pitesti, 138))
    craiova.add_adjacent(Adjacent(rimnicu, 146))

    rimnicu.add_adjacent(Adjacent(craiova, 146))
    rimnicu.add_adjacent(Adjacent(sibiu, 80))
    rimnicu.add_adjacent(Adjacent(pitesti, 97))

    fagaras.add_adjacent(Adjacent(sibiu, 99))
    fagaras.add_adjacent(Adjacent(bucharest, 211))

    pitesti.add_adjacent(Adjacent(rimnicu, 97))
    pitesti.add_adjacent(Adjacent(craiova, 138))
    pitesti.add_adjacent(Adjacent(bucharest, 101))

    bucharest.add_adjacent(Adjacent(fagaras, 211))
    bucharest.add_adjacent(Adjacent(pitesti, 101))
    bucharest.add_adjacent(Adjacent(giurgiu, 90))


class Greedy_Algorithm:
    heuristic = {
        "Arad": 366,
        "Bucharest": 0,
        "Craiova": 160,
        "Dobreta": 242,
        "Eforie": 161,
        "Fagaras": 178,
        "Giurgiu": 77,
        "Hirsova": 151,
        "Iasi": 226,
        "Lugoji": 244,
        "Mehadia": 241,
        "Neamt": 234,
        "Oradea": 380,
        "Pitesti": 98,
        "Rimnicu": 193,
        "Sibiu": 253,
        "Timisoara": 329,
        "Urziceni": 80,
        "Vaslui": 199,
        "Zerind": 374
    }

    def __init__(self, origin: str, graph: Graph):
        self.path: Dict[str, int] = {}
        self.origin = origin
        self.graph = graph

    def show_route(self):
        if self.path.items() == 0:
            print("No paths processed.")
            return

        print(f"The fastest way is {self.origin}", end=" ")
        total = sum(self.path.values())
        for index, (key, value) in enumerate(self.path.items()):
            print(f"- {value} > {key}", end="")

        print(f" Total distance: {total}")

    def search(self):
        if self.origin == "Bucharest":
            print("You are already at your destination!")
            return

        vertex = self.graph.__getattribute__(self.origin)
        while True:
            vertex.visited = True
            distances = []
            if len(vertex.adjacents) > 0:
                for adjacent in vertex.adjacents:
                    distances.append(self.heuristic[adjacent.vertex.title])

                distances.sort()
                finded_vertice = False

                for distance in distances:
                    if finded_vertice:
                        break
                    key = find_key_by_value(self.heuristic, distance)
                    for adjacent in vertex.adjacents:
                        if key == adjacent.vertex.title and adjacent.vertex.visited is False:
                            if key == "Bucharest":
                                self.path[key] = adjacent.cust
                                return
                            vertex = adjacent.vertex
                            self.path[key] = adjacent.cust
                            finded_vertice = True
                            break


busca = Greedy_Algorithm("arad", Graph())
busca.search()
busca.show_route()
