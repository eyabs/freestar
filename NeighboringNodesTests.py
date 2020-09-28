import unittest
from itertools import product
from NeighboringNodes import *

class TestNeighboringNodes(unittest.TestCase):
    def test_build_grid(self):
        expected_grid = [
            [{'x': 0, 'y': 0, 'i': 0}, {'x': 1, 'y': 0, 'i': 1}], 
            [{'x': 0, 'y': 1, 'i': 2}, {'x': 1, 'y': 1, 'i': 3}]
        ]
        size = 2
        nn = NeighboringNodes(size, False)
        grid = nn.build_grid()

        # Check the x-dimension is the correct size.
        self.assertEqual(len(expected_grid), len(grid))

        # Check the y-dimension is the correct size.
        self.assertEqual(
            len([1 for g in expected_grid]), 
            len([1 for g in grid])
        )

        # Check each item is correct.
        for i, coords in enumerate(product(range(size), repeat=2)):
            x, y = coords
            self.assertEqual(expected_grid[x][y], grid[x][y])

    def test_get_coords_from_index(self):
        size = 3
        nn = NeighboringNodes(size)
        
        for i, c in enumerate(product(range(size), repeat=2)):
            expected_coords = (c[1], c[0])
            coords = nn.get_coords_from_index(i)
            self.assertEqual(expected_coords, coords)

    def test_find_neighbors_args_error(self):
        size = 3
        nn = NeighboringNodes(size)
        nn.find_neighboring_nodes(x=1, y=1, m=1, type='SQUARE')
        
        with self.assertRaises(Exception) as e:
            nn.find_neighboring_nodes(x=1, y=1, i=1, m=1, type='SQUARE')
            print(f"e: {e.exception}")
        self.assertTrue('Invalid Arguments' in str(e.exception))
        
        with self.assertRaises(Exception) as e:
            nn.find_neighboring_nodes(x=1, y=1, m=1, type='INVALID_TYPE')
            print(f"e: {e.exception}")
        self.assertTrue('Invalid Arguments' in str(e.exception))


    def test_find_neighbors_square(self):
        expected = set([
            (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
            (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), 
            (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), 
            (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), 
            (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
        ])

        size = 7
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=3, y=3, m=2, type='SQUARE')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

    def test_find_neighbors_cross(self):
        expected = set([
                            (3, 1),
                            (3, 2),
            (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), 
                            (3, 4), 
                            (3, 5)
        ])

        size = 7
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=3, y=3, m=2, type='CROSS')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

    def test_find_neighbors_diamond(self):
        expected = set([
                                    (3, 2),
                            (2, 3), (3, 3), (4, 3),
                    (1, 4), (2, 4), (3, 4), (4, 4), (5, 4),
            (0, 5), (1, 5), (2, 5), (3, 5), (4, 5), (5, 5), (6, 5),
                    (1, 6), (2, 6), (3, 6), (4, 6), (5, 6),
                            (2, 7), (3, 7), (4, 7),
                                    (3, 8)
        ])

        size = 9
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=3, y=5, m=3, type='DIAMOND')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

    def test_find_neighbors_square_bad_coords(self):
        expected = set([
            (0, 0), (1, 0), (2, 0), (3, 0), (4, 0), (5, 0), 
            (0, 1), (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), 
            (0, 3), (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), 
            (0, 4), (1, 4), (2, 4), (3, 4), (4, 4), (5, 4)
        ])

        size = 7
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=2, y=1, m=3, type='SQUARE')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

    def test_find_neighbors_cross_bad_coords(self):
        expected = set([
                    (1, 0),
                    (1, 1),
            (0, 2), (1, 2), (2, 2), (3, 2), (4, 2),
                    (1, 3),
                    (1, 4),
                    (1, 5)
        ])

        size = 7
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=1, y=2, m=3, type='CROSS')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

    def test_find_neighbors_diamond_bad_coords(self):
        expected = set([
                            (3, 0), (4, 0), (5, 0), 
                    (2, 1), (3, 1), (4, 1), (5, 1), 
            (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), 
                    (2, 3), (3, 3), (4, 3), (5, 3), 
                            (3, 4), (4, 4), (5, 4), 
                                    (4, 5)
        ])

        size = 6
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=4, y=2, m=3, type='DIAMOND')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

    def test_find_neighbors_OOB_coords(self):
        # Left of the grid
        expected = set([
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1), (2, 1),
            (0, 2), (1, 2), (2, 2),
            (0, 3), (1, 3), (2, 3)
        ])

        size = 7
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=-1, y=1, m=2, type='SQUARE')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)

        # Above the grid
        expected = set([
            (0, 0), (1, 0), (2, 0),
            (0, 1), (1, 1), (2, 1)
        ])

        size = 7
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=1, y=-1, m=1, type='SQUARE')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)
        # Below and to the right of the grid
        expected = set([
            (1, 1), (2, 1),
            (1, 2), (2, 2)
        ])

        size = 3
        nn = NeighboringNodes(size)
        neighbors = nn.find_neighboring_nodes(x=100, y=100, m=1, type='SQUARE')
        neighbors = set(neighbors)
        self.assertEqual(expected, neighbors)


if __name__ == '__main__':
    unittest.main()
