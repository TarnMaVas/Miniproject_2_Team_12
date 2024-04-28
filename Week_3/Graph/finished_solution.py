'''graph'''
def get_graph_from_file(file_name):
    with open(file_name, "r", encoding="utf-8") as file:
        content = file.readlines()
        listok = []
        for coordinates in content:
            nums = coordinates.split()
            for i in nums:
                for digits in i:
                    if digits.isdigit():
                        listok.append(int(digits))
    split_listok = [listok[i : i + 2] for i in range(0, len(listok), 2)]
    return split_listok

def to_edge_dict(edge_list):
    if edge_list==[]:
        return {}
    plur = set()
    listok = []
    listochishche = []
    for el in edge_list:
        plur.add(el[0])
        plur.add(el[1])
    for didg in plur:
        for el in edge_list:
            if didg == el[0]:
                listok.append(el[1])
            if didg == el[1]:
                listok.append(el[0])
        listochishche.append(list(sorted(listok)))
        listok = []
        dictor = dict(zip(plur, listochishche))
    return dictor

def is_edge_in_graph(graph, edge):
    for key in graph:
        if key == edge[1]:
            for i in graph[key]:
                if edge[0] == i:
                    return True
                return False

def add_edge(graph, edge):
    v1, v2 = edge
    if v1 in graph:
        if v2 not in graph[v1]:
            graph[v1].append(v2)
    else:
        graph[v1] = [v2]
    if v2 in graph:
        if v1 not in graph[v2]:
            graph[v2].append(v1)
    else:
        graph[v2] = [v1]
    return graph

def del_edge(graph, edge):
    # """
    # (dict, tuple) -> (dict)

    # Delete an edge from the graph and return a new graph.

    # >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    # {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    # """
    # if edge[0] in graph and edge[1] in graph:
    #     (graph[edge[0]]).remove(edge[1])
    #     (graph[edge[1]]).remove(edge[0])
    # return graph
    v1, v2 = edge
    if v1 in graph and v2 in graph:
        if v2 in graph[v1]:
            graph[v1].remove(v2)
        if v1 in graph[v2]:
            graph[v2].remove(v1)
    return graph


def add_node(graph, node):
    # """
    # (dict, int) -> (dict)

    # Add a new node to the graph and return a new graph.

    # >>> add_node({1: [2], 2: [1]}, 3)
    # {1: [2], 2: [1], 3: []}
    # """
    if not node in graph:
        graph[node] = []
    return graph

def del_node(graph, node):
    x = node
    for i in graph.copy():
        if i == x:
            del graph[i]
    for h in graph.values():
        if x in h:
            h.remove(x)
    return graph

def convert_to_dot(filename: str) -> None:
    with open(filename, "r", encoding="utf-8") as file:
        content = file.readlines()
    data=[i.strip().split(",") for i in content]
    for i in range(len(data)):
        data.append(data[i][::-1])
    for i in data:
        i.insert(1, '->')
    data = sorted(data, key=lambda number: number[0])
    with open(filename.replace('.txt', '.dot'), "w", encoding="utf-8") as file:
        file.write('digraph {\n')
        for line in data:
            file.write((''.join(line)+'\n'))
        _ = file.write('}')
