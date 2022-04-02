from pprint import pprint

# def make_adjacency_list(*args):
#     adjacency_list = dict()
#     for edge_pair in args:
#         node = edge_pair[0]
#         if node in adjacency_list:
#             adjacency_list[node].append(edge_pair[1])
#         else:
#             adjacency_list[node] = [edge_pair[1]]
#     return adjacency_list

def count_nodes(*args):
    set_of_nodes = set()
    for edge_pair in args:
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[1])
    return set_of_nodes, len(set_of_nodes)

# def make_adjacency_matrix(*args):
#     count = count_nodes(*args)[1]
#     adjacency_matrix = []
#     list_to_append = []
#     for value in range(count + 1):
#         list_to_append.append(0)
#
#     for value in range(count + 1):
#         adjacency_matrix.append(list_to_append[:])
#
#     for edge_value in args:
#         adjacency_matrix[edge_value[0]][edge_value[1]] = 1
#
#     pprint(adjacency_matrix)
#
#     return adjacency_matrix

def make_directional_adjacency_list(*args):
    adjacency_list = dict()
    for edge_pair in args:
        node = edge_pair[0]

        if edge_pair[2] == "<>" or edge_pair[2] == "->":
            if node in adjacency_list:
                if edge_pair[1] not in adjacency_list[node]:
                    adjacency_list[node].append(edge_pair[1])

            else:
                adjacency_list[node] = [edge_pair[1]]

        if edge_pair[2] == "<>" or edge_pair[2] == "<-":
            if edge_pair[1] in adjacency_list:
                if node not in adjacency_list[edge_pair[1]]:
                    adjacency_list[edge_pair[1]].append(node)
            else:
                adjacency_list[edge_pair[1]] = [node]

    return adjacency_list

def make_directional_adjacency_matrix(*args):
    count = count_nodes(*args)[1]
    adjacency_matrix = []
    list_to_append = []
    for value in range(count + 1):
        list_to_append.append(0)

    for value in range(count + 1):
        adjacency_matrix.append(list_to_append[:])

    for edge_value in args:
        if edge_value[2] == "<>" or edge_value[2] == "->":
            adjacency_matrix[edge_value[0]][edge_value[1]] = 1

        if edge_value[2] == "<>" or edge_value[2] == "<-":
            adjacency_matrix[edge_value[1]][edge_value[0]] = 1

    pprint(adjacency_matrix)

    return adjacency_matrix

class AdjacencyList:
    def __init__(self, Nodes, is_directed = False):
        self.nodes = Nodes
        self.adjacency_list = {}
        self.is_directed = is_directed
        for node in self.nodes:
            self.adjacency_list[node] = []

    def print(self):
        pprint(self.adjacency_list)

    def add_edge_pair(self, node, value, direction = "<>"):
        if self.is_directed:
            if direction == "->":
                if value not in self.adjacency_list[node]:
                    self.adjacency_list[node].append(value)
            elif direction == "<-":
                if node not in self.adjacency_list[value]:
                    self.adjacency_list[value].append(node)
            else:
                self.adjacency_list[node].append(value)
                self.adjacency_list[value].append(node)
        else:
            self.adjacency_list[node].append(value)
            self.adjacency_list[value].append(node)

    def count_most_edges(self):
        edge_dictionary = {}
        # init
        for node in self.nodes:
            edge_dictionary[node] = 0
        # leaving
        for node in self.nodes:
            edge_dictionary[node] += len(self.adjacency_list[node])
        # pointing towards
        for node in edge_dictionary:
            for value in self.adjacency_list[node]:
                edge_dictionary[value] += 1

        print(max(edge_dictionary, key = edge_dictionary.get))
        return max(edge_dictionary, key = edge_dictionary.get)

    def count_most_edges_leaving(self):
        edge_dictionary = {}
        for node in self.nodes:
            edge_dictionary[node] = 0

        for node in self.nodes:
            edge_dictionary[node] += len(self.adjacency_list[node])

        print(max(edge_dictionary, key=edge_dictionary.get))
        return max(edge_dictionary, key=edge_dictionary.get)

    def count_most_edges_pointing(self):
        edge_dictionary = {}
        for node in self.nodes:
            edge_dictionary[node] = 0

        for node in edge_dictionary:
            for value in self.adjacency_list[node]:
                edge_dictionary[value] += 1

        print(max(edge_dictionary, key=edge_dictionary.get))
        return max(edge_dictionary, key=edge_dictionary.get)

class AdjacencyMatrix:
    def __init__(self, size, is_directed = False):
        self.adjacency_matrix = []
        self.size = size
        self.is_directed = is_directed

        self.edge_total = {}
        self.edge_leaving = {}
        self.edge_pointing = {}

        list_to_append = []
        for i in range(size):
            self.edge_total[i] = 0
            self.edge_leaving[i] = 0
            self.edge_pointing[i] = 0

            list_to_append.append(0)

        for i in range(size):
            self.adjacency_matrix.append(list_to_append[:])

    def print(self):
        pprint(self.adjacency_matrix)

    def add_edge_pair(self, node, value, direction = "<>"):

        if self.is_directed:
            if direction == "->":
                self.adjacency_matrix[node][value] = 1

                self.edge_total[node] += 1
                self.edge_leaving[node] += 1
                self.edge_pointing[value] += 1

            elif direction == "<-":
                self.adjacency_matrix[value][node] = 1

                self.edge_total[value] += 1
                self.edge_leaving[value] += 1
                self.edge_pointing[node] += 1

            else:
                self.adjacency_matrix[node][value] = 1
                self.adjacency_matrix[value][node] = 1

                self.edge_total[node] += 1
                self.edge_leaving[node] += 1
                self.edge_pointing[node] += 1

                self.edge_total[value] += 1
                self.edge_leaving[value] += 1
                self.edge_pointing[value] += 1
        else:
            self.adjacency_matrix[node][value] = 1
            self.adjacency_matrix[value][node] = 1

            self.edge_total[node] += 1
            self.edge_leaving[node] += 1
            self.edge_pointing[node] += 1

            self.edge_total[value] += 1
            self.edge_leaving[value] += 1
            self.edge_pointing[value] += 1

    def count_most_edges(self):
        print(max(self.edge_total, key=self.edge_total.get))
        return max(self.edge_total, key=self.edge_total.get)

    def count_most_edges_leaving(self):
        print(max(self.edge_leaving, key=self.edge_leaving.get))
        return max(self.edge_leaving, key=self.edge_leaving.get)

    def count_most_edges_pointing(self):
        print(max(self.edge_pointing, key=self.edge_pointing.get))
        return max(self.edge_pointing, key=self.edge_pointing.get)


if __name__ == "__main__":
    # make_list_case = make_adjacency_list((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4))
    # make_list_case = make_adjacency_list((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6))
    # count_test_1 = count_nodes((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4))
    # count_test_2 = count_nodes((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6))
    # make_matrix_case = make_adjacency_matrix((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6))

    # make_directional_list_case = make_directional_adjacency_list((1, 2, "->"), (1, 3, "<-"), (2, 3, "<>"), (2, 4, "<-"), (3, 1, "->"), (3, 4, "<>"))
    # count_test = count_nodes((1, 2, "->"), (1, 3, "<-"), (2, 3, "<>"))
    # make_directional_matrix_case = make_directional_adjacency_matrix((1, 2, "->"), (1, 3, "<-"), (2, 3, "<>"), (2, 4, "<-"), (3, 1, "->"), (3, 4, "<>"))

    print("--------------------------")

    nodes = [0, 1, 2, 3, 4]
    list = AdjacencyList(nodes, True)

    list.add_edge_pair(1, 2, "->")
    list.add_edge_pair(1, 3, "<-")
    list.add_edge_pair(2, 3, "<>")
    list.add_edge_pair(2, 4, "<-")
    list.add_edge_pair(3, 1, "->")
    list.add_edge_pair(3, 4, "<>")

    # list.print()
    list.count_most_edges()
    list.count_most_edges_leaving()
    list.count_most_edges_pointing()

    matrix = AdjacencyMatrix(5, True)
    matrix.add_edge_pair(1, 2, "->")
    matrix.add_edge_pair(1, 3, "<-")
    matrix.add_edge_pair(2, 3, "<>")
    matrix.add_edge_pair(2, 4, "<-")
    matrix.add_edge_pair(3, 1, "->")
    matrix.add_edge_pair(3, 4, "<>")

    # matrix.print()
    matrix.count_most_edges()
    matrix.count_most_edges_leaving()
    matrix.count_most_edges_pointing()