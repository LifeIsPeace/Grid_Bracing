from collections import deque
from enum import Enum


class RowColumn(Enum):
    ROW = 0
    COLUMN = 1


def grid_rigidity(braced_squares: list[list[bool]]) -> str:
    rows: int = len(braced_squares)
    columns: int = len(braced_squares[0])
    visited: list[tuple[int, int]] = []
    # The interpreter is surprised that the list has different types, ignore error
    queue: deque[list[int, int, RowColumn]] = deque()
    row_traversal: bool = True

    row_index: int = 0
    column_index: int = 0

    number_of_braces: int = 0
    for row in braced_squares:
        for brace in row:
            if brace:
                number_of_braces += 1

    def progress_queue() -> None:
        temp_tuple: tuple[int, int] = (row_index, column_index)
        if temp_tuple not in visited:
            visited.append((row_index, column_index))
        queue.popleft()

    def has_visited(index:int, row_or_column: bool) -> bool:
        if row_or_column:
            this_tuple = (index, column_index)
        else:
            this_tuple = (row_index, index)
        return this_tuple in visited

    # First iteration. A general method would look a little different
    temp_column = 0
    for brace in braced_squares[0]:
        if brace:
            queue.append([row_index, column_index, RowColumn.COLUMN])
        temp_column += 1

    if len(queue) == 0:
        return "Not Rigid"

    first_iteration: int = 1
    while len(queue) != 0:

        if(first_iteration == 1):
            row_index = queue[0][0]
            column_index = queue[0][1]
            if queue[0][2] is RowColumn.ROW:
                row_traversal = True
            else:
                row_traversal = False
            queue.pop()
            temp_row = 0
            for temp_row in range(rows):
                if braced_squares[temp_row][column_index] and not has_visited(temp_row, True):
                    queue.append([temp_row, column_index, RowColumn.ROW])
            first_iteration = 0
            continue

        if row_traversal:
            row_index = queue[0][0]
            column_index = queue[0][1]
            if queue[0][2] is RowColumn.ROW:
                row_traversal = True
            else:
                row_traversal = False
            progress_queue()
            temp_row = 0
            for temp_row in range(rows):
                if braced_squares[temp_row][column_index] and not has_visited(temp_row, True):
                    queue.append([temp_row, column_index, RowColumn.ROW])

        else:
            row_index = queue[0][0]
            column_index = queue[0][1]
            if queue[0][2] is RowColumn.ROW:
                row_traversal = True
            else:
                row_traversal = False
            progress_queue()
            temp_column = 0
            for brace in braced_squares[row_index]:
                if brace and not has_visited(temp_column, False):
                    queue.append([row_index, temp_column, RowColumn.COLUMN])
                temp_column += 1
    if len(visited) < rows + columns - 1:
        return "The Graph Is Not Rigid"
    # An optimally braced m x n graph has m + n - 1 braces
    elif len(visited) > rows + columns - 1:
        return "The Graph Is Non-Optimally Rigid"
    else:
        return "The Graph Is Optimally Rigid"
