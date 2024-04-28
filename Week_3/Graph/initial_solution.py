'''graph'''
def get_graph_from_file(file_name):
    """
    (str) -> (list)

    Read graph from file and return a list of edges.

    >>> get_graph_from_file("data1.txt")
    [[1, 2], [3, 4], [1, 5]]
    """
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
    """
    (list) -> (dict)

    Convert a graph from list of edges to dictionary of vertices.

    >>> to_edge_dict([[1, 2], [3, 4], [1, 5], [2, 4]])
    {1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}
    """
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
    """
    (dict, tuple) -> bool

    Return True if graph contains a given edge and False otherwise.

    >>> is_edge_in_graph({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    False
    """
    for key in graph:
        if key == edge[1]:
            for i in graph[key]:
                if edge[0] == i:
                    return True
                return False

def add_edge(graph, edge):
    """
    (dict, tuple) -> dict

    Add a new edge to the graph and return new graph.

    >>> add_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (3, 1))
    {1: [2, 5, 3], 2: [1, 4], 3: [4, 1], 4: [2, 3], 5: [1]}
    """
    for key in graph:
        if key == edge[0]:
            graph[key].append(edge[1])
            b = []
            for i in graph[key]:
                if i not in b:
                    b.append(i)
            graph[key] = b
        elif key == edge[1]:
            graph[key].append(edge[0])
            b = []
            for i in graph[key]:
                if i not in b:
                    b.append(i)
            graph[key] = b
    for i in graph.items():
        b = []
        for d in i:
            if d not in b:
                b.append(d)
    return graph

def del_edge(graph, edge):
    """
    (dict, tuple) -> (dict)

    Delete an edge from the graph and return a new graph.

    >>> del_edge({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, (2, 4))
    {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
    """
    if edge[0] in graph and edge[1] in graph:
        (graph[edge[0]]).remove(edge[1])
        (graph[edge[1]]).remove(edge[0])
    return graph


def add_node(graph, node):
    """
    (dict, int) -> (dict)

    Add a new node to the graph and return a new graph.

    >>> add_node({1: [2], 2: [1]}, 3)
    {1: [2], 2: [1], 3: []}
    """
    if not node in graph:
        graph[node] = []
    return graph

def del_node(graph, node):
    """
    (dict, int) -> (dict)

    Delete a node and all incident edges from the graph.

    >>> del_node({1: [2, 5], 2: [1, 4], 3: [4], 4: [2, 3], 5: [1]}, 4)
    {1: [2, 5], 2: [1], 3: [], 5: [1]}
    """
    x = node
    for i in graph.copy():
        if i == x:
            del graph[i]
    for h in graph.values():
        if x in h:
            h.remove(x)
    return graph

def convert_to_dot(filename: str) -> None:
    """
    Get graph from a file and save the directed graph to a file in a DOT format with the same name.
    >>> import tempfile
    >>> with tempfile.NamedTemporaryFile(mode='w', encoding='utf-8', delete=False) as tmpfile:
    ...     _ = tmpfile.write('1,2')
    >>> convert_to_dot(tmpfile.name)
    >>> with open(tmpfile.name, 'r', encoding='utf-8') as file:
    ...    file.read()
    'digraph {\\n1->2\\n2->1\\n}'
    """
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

if __name__ == "__main__":
    import doctest

    print(doctest.testmod())
