from itertools import product

class NeighboringNodes(object):
    def __init__(self, size, debug=False):
        self.size = size
        self.debug = debug

    def build_grid(self):
        i = 0

        grid = []
        for y in range(self.size):
            grid.append([])
            for x in range(self.size):
                node = {'x': x, 'y': y, 'i': i}
                grid[y].append(node)
                i += 1

        if self.debug:
            print(grid)

        return grid

    def get_coords_from_index(self, index):
        x = index % self.size
        y = int(index / self.size)
        return (x, y)

    def get_index_from_coords(self, x, y):
        index = y * self.size + x
        return index

    def find_neighboring_nodes(self, x=None, y=None, i=None, m=None, type=None):
        x_and_y = (x is not None and y is not None)

        if (not x_and_y and i is not None) or (x_and_y and not i is None):
            raise Exception("Invalid Arguments: Must provide x & y OR i but not both.")
        if not type or type.upper() not in ['SQUARE', 'CROSS', 'DIAMOND']:
            raise Exception("Invalid Arguments: type must be 'SQUARE', 'CROSS', or 'DIAMOND'.")
        

        if not x_and_y:
            # Make sure i is between 0 and size ** 2 - 1
            if i > self.size ** 2 - 1:
                i = self.size ** 2 - 1

            if i < 0:
                i = 0

            x, y = self.get_coords_from_index(i)

        # If the coordinates are out of bounds, set to closest point
        x = min(max(0, x), self.size-1)
        y = min(max(0, y), self.size-1)

        if type.upper() == 'SQUARE':
            coords = self._find_neighbors_square(x, y, m)

        elif type.upper() == 'CROSS':
            coords = self._find_neighbors_cross(x, y, m)

        elif type.upper() == 'DIAMOND':
            coords = self._find_neighbors_diamond(x, y, m)

        return coords

    def _find_neighbors_square(self, center_x, center_y, m):

        min_x = center_x - m
        max_x = center_x + m

        min_y = center_y - m
        max_y = center_y + m

        # Ensure we don't exceed the grid's boundaries.
        min_x = min(max(0, min_x), self.size-1)
        max_x = min(max(0, max_x), self.size-1)
        
        min_y = min(max(0, min_y), self.size-1)
        max_y = min(max(0, max_y), self.size-1)
        
        print("SQUARE\n" \
         f" center_x, center_y, m: {center_x}, {center_y}, {m}\n" \
         f"min_x {min_x}\n" \
         f"max_x {max_x}\n" \
         f"min_y {min_y}\n" \
         f"max_y {max_y}\n"
         )

        coords = [(x, y) for y in range(min_y, max_y+1) for x in range(min_x, max_x+1)]

        return coords


    def _find_neighbors_cross(self, center_x, center_y, m):

        min_x = center_x - m
        max_x = center_x + m

        min_y = center_y - m
        max_y = center_y + m
        
        # Ensure we don't exceed the grid's boundaries.
        min_x = min(max(0, min_x), self.size-1)
        max_x = min(max(0, max_x), self.size-1)
        
        min_y = min(max(0, min_y), self.size-1)
        max_y = min(max(0, max_y), self.size-1)

        print("CROSS\n" \
         f" center_x, center_y, m: {center_x}, {center_y}, {m}\n" \
         f"min_x {min_x}\n" \
         f"max_x {max_x}\n" \
         f"min_y {min_y}\n" \
         f"max_y {max_y}\n"
         )

        coords = []
        for y in range(min_y, max_y + 1):
            if y == center_y:
                for x in range(min_x, max_x+1):
                    coords.append((x, y))
                    print((x,y), end='')
            else:
                coords.append((center_x, y))
                print((center_x,y), end='')
            print()
        print()
        return coords
        
    def _find_neighbors_diamond(self, center_x, center_y, m):

        min_y = center_y - m
        max_y = center_y + m
        
        # Ensure we don't exceed the grid's boundaries.
        min_y = min(max(0, min_y), self.size-1)
        max_y = min(max(0, max_y), self.size-1)


        print("DIAMOND" \
         f" center_x, center_y, m: {center_x}, {center_y}, {m}" \
         f"min_y {min_y}" \
         f"max_y {max_y}"
         )
        
        coords = []
        for y in range(min_y, max_y + 1):
            offset = m - abs(y - center_y)
            for x in range(center_x - offset, center_x + offset + 1):
                if x >= 0 and x < self.size:
                    coords.append((x, y))
                    print((x,y), end='')
            print()
        print()
        return coords
        
