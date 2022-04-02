from pprint import pprint

def make_adjacency_list(*args):
    adjacency_list = dict()
    for edge_pair in args:
        node = edge_pair[0]
        if node in adjacency_list:
            adjacency_list[node].append(edge_pair[1])
        else:
            adjacency_list[node] = [edge_pair[1]]
    return adjacency_list

def count_nodes(*args):
    set_of_nodes = set()
    for edge_pair in args:
        set_of_nodes.add(edge_pair[0])
        set_of_nodes.add(edge_pair[1])
    return set_of_nodes, len(set_of_nodes)

def make_adjacency_matrix(*args):
    count = count_nodes(*args)[1]
    adjacency_matrix = []
    list_to_append = []
    for value in range(count + 1):
        list_to_append.append(0)

    for value in range(count + 1):
        adjacency_matrix.append(list_to_append[:])

    for edge_value in args:
        adjacency_matrix[edge_value[0]][edge_value[1]] = 1

    pprint(adjacency_matrix)

    return adjacency_matrix

def make_directional_adjacency_list(*args):
    adjacency_list = dict()
    for edge_pair in args:
        node = edge_pair[0]

        if edge_pair[2] == "<>" or edge_pair[2] == "->":
            if node in adjacency_list:
                adjacency_list[node].append(edge_pair[1])

            else:
                adjacency_list[node] = [edge_pair[1]]

        if edge_pair[2] == "<>" or edge_pair[2] == "<-":
            if edge_pair[1] in adjacency_list:
                adjacency_list[edge_pair[1]].append(edge_pair[0])

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

if __name__ == "__main__":
    # make_list_case = make_adjacency_list((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4))
    # make_list_case = make_adjacency_list((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6))
    # count_test_1 = count_nodes((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4))
    # count_test_2 = count_nodes((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6))
    # make_matrix_case = make_adjacency_matrix((1, 2), (1, 3), (2, 1), (2, 4), (3, 1), (3, 4), (4, 2), (4, 3), (4, 5), (5, 4), (5, 6))

    make_directional_adjacency_list((1, 2, "->"), (1, 3, "<-"), (2, 3, "<>"))
    count_test = count_nodes((1, 2, "->"), (1, 3, "<-"), (2, 3, "<>"))
    make_directional_adjacency_matrix((1, 2, "->"), (1, 3, "<-"), (2, 3, "<>"))




