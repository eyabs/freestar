# Freestar.io Assessment

## Neighboring Nodes

### Software Versions

This assessment was completed using an Anaconda distribution of Python 3.6.10 and SQLite version 3.13.0.

The solutions to Task 1 and Task 2 are provided in the file `NeighboringNodes.py`. Unit tests are provided in the file `NeighboringNodesTests.py`

The solution to Task 3 is provided in the file `q3.sql`. Sample data may be loaded with the file `create_q3.sql`.

### Task 1: Build the Grid

This question required a class containing a method which would take in the parameters `size: int` and `debug: bool` to produce a grid of `size x size` instantiated with nodes containing their index, x coordinate, and y-coordinate. If `debug` is set to true, the `build_grid()` method will print the grid of nodes.

This requirement was satisfied with the `build_grid` method of the `NeighboringNodes` class.

Sample Usage:

```python
from NeighboringNodes import *
size = 2
nn = NeighboringNodes(size, False)
grid = nn.build_grid()

'''
Grid will resemble:
[
    [{'x': 0, 'y': 0, 'i': 0}, {'x': 1, 'y': 0, 'i': 1}], 
    [{'x': 0, 'y': 1, 'i': 2}, {'x': 1, 'y': 1, 'i': 3}]
]
'''
```

Additionally, this question required a method which accepts the index of a node and returns the (x, y) coordinate of that node. This requirement was satisfied with the `get_coords_from_index` method of the `NeighboringNodes` class.

Sample Usage:

```python
from NeighboringNodes import *
size = 3
nn = NeighboringNodes(size)
nn.get_coords_from_index(5)
'''
Output:
(2, 1)
'''
```

### Task 2: Finding neighbors

This question required the addition of a method for the `NeighboringNodes` class, which found all the neighbors of a node within a distance of `m` using a neighborhood topology of type `'SQUARE'`, `'CROSS'` or `'DIAMOND'`. This method was implemented as `find_neighboring_nodes`. This method accepts the following parameters:

* ​`x`:​ ​x-axis coordinate
* ​`y`:​ ​y-axis coordinate
* ​`i`:​ ​nodeindex
* ​`m​​`: neighborhood radius (int, 0 < ​​m​​ <= ​​size/2​)​
* ​`type`:​ ​neighborhood type(enum:SQUARE,CROSS,DIAMOND)

Additionally, this method accepts either `x` AND `y`, or only `i`, but not both.

Sample Usage:

```python
from NeighboringNodes import *
size = 7
nn = NeighboringNodes(size)
neighbors = nn.find_neighboring_nodes(x=3, y=3, m=2, type='SQUARE')

'''
Output will resemble:
[
    (1, 1), (2, 1), (3, 1), (4, 1), (5, 1), 
    (1, 2), (2, 2), (3, 2), (4, 2), (5, 2), 
    (1, 3), (2, 3), (3, 3), (4, 3), (5, 3), 
    (1, 4), (2, 4), (3, 4), (4, 4), (5, 4), 
    (1, 5), (2, 5), (3, 5), (4, 5), (5, 5)
]
'''
```

### Task 3: SQL

This question asked: Given a table having records of user visits in the following format: `user_id, visit_date, url`, find out the longest consecutive days each user has visited.

This was accomplished using a recursive CTE in SQLite found in the file `q3.sql` and uses test data which may be found in `create_q3.sql`. To load the data and run the query, run the following commands in a terminal:

```
sqlite3
.headers on
.read create_q3.sql
.read q3.sql
```
Output:
```
UserName|CONSEC
user1|4
user2|4
user3|2
```












