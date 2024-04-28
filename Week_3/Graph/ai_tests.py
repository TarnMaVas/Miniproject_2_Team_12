import unittest
from graph import *
import os

class TestGetGraphFromFile(unittest.TestCase):
    def test_empty_file(self):
        # Arrange
        file_name = "empty.txt"
        
        # Act
        result = get_graph_from_file(file_name)
        
        # Assert
        self.assertEqual(result, [])

    def test_non_empty_file(self):

        file_name = "data1.txt"  # Assuming data1.txt contains: "1,2\n3,4\n1,5"
        result = get_graph_from_file(file_name)
        self.assertEqual(result, [[1, 2], [3, 4], [1, 5]])

class TestToEdgeDict(unittest.TestCase):
    def test_empty_list(self):
        edge_list = []
        result = to_edge_dict(edge_list)
        self.assertEqual(result, {})

    def test_non_empty_list(self):
        edge_list = [[1, 2], [3, 4], [1, 5]]
        result = to_edge_dict(edge_list)
        expected_dict = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        self.assertEqual(result, expected_dict)

class TestIsEdgeInGraph(unittest.TestCase):
    def test_edge_in_graph(self):
        # Arrange
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        edge = [1, 2]
        
        # Act
        result = is_edge_in_graph(graph, edge)
        
        # Assert
        self.assertTrue(result)

    def test_edge_not_in_graph(self):
        # Arrange
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        edge = [2, 3]
        
        # Act
        result = is_edge_in_graph(graph, edge)
        
        # Assert
        self.assertFalse(result)

class TestAddEdge(unittest.TestCase):
    def test_add_new_edge(self):
        # Arrange
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        edge = (2, 3)
        
        # Act
        result = add_edge(graph, edge)
        
        # Assert
        expected_graph = {1: [2, 5], 2: [1, 3], 3: [4, 2], 4: [3], 5: [1]}
        self.assertEqual(result, expected_graph)

    def test_add_existing_edge(self):
        # Arrange
        graph = {1: [2, 5], 2: [1], 3: [4], 4: [3], 5: [1]}
        edge = (1, 2)
        result = add_edge(graph, edge)
        self.assertEqual(result, graph)

class TestDelEdge(unittest.TestCase):
    def test_remove_existing_edge(self):
        graph = {1: [2, 5], 2: [1, 3], 3: [4], 4: [3], 5: [1]}
        edge = [1, 2]
        result = del_edge(graph, edge)
        expected_graph = {1: [5], 2: [3], 3: [4], 4: [3], 5: [1]}
        self.assertEqual(result, expected_graph)

    def test_remove_non_existing_edge(self):
        # Arrange
        graph = {1: [2, 5], 2: [1, 3], 3: [4], 4: [3], 5: [1]}
        edge = [2, 4]
        
        # Act
        result = del_edge(graph, edge)
        
        # Assert
        self.assertEqual(result, graph)

class TestAddNode(unittest.TestCase):
    def test_add_new_node(self):
        # Arrange
        graph = {1: [2, 5], 2: [1, 3], 3: [4], 4: [3], 5: [1]}
        node = 6
        
        # Act
        result = add_node(graph, node)
        
        # Assert
        expected_graph = {1: [2, 5], 2: [1, 3], 3: [4], 4: [3], 5: [1], 6: []}
        self.assertEqual(result, expected_graph)

    def test_add_existing_node(self):
        # Arrange
        graph = {1: [2, 5], 2: [1, 3], 3: [4], 4: [3], 5: [1]}
        node = 3
        
        # Act
        result = add_node(graph, node)
        
        # Assert
        self.assertEqual(result, graph)

class TestConvertFunctions(unittest.TestCase):
    def test_del_node(self):
        # Тестовий випадок 1: Видалення вершини з непорожнього графа
        graph1 = {'A': ['B', 'C'], 'B': ['A'], 'C': ['A']}
        del_node(graph1, 'A')
        self.assertNotIn('A', graph1)
        self.assertNotIn('B', graph1['C'])
        self.assertNotIn('C', graph1['B'])

        # Тестовий випадок 2: Видалення вершини з порожнього графа
        graph2 = {}
        del_node(graph2, 'A')
        self.assertNotIn('A', graph2)
