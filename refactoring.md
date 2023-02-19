# Refactoring

## polynom_for_points

### Refactoring plan

In order to decrease the complexity, the function can be split into smaller subfunctions.
There are four areas of the code with high complexity, that could be moved outside the function to helper functions. These areas and their corresponding subfunctions are:
* Adding the x and x to the power of values to a matrix.
    * Moved to `add_x_values(coordinates, x) -> matrix`
* Adding the y values to a vector.
    * Moved to `add_y_values(coordinates, x) -> vector`
* Manipulation the matrix.
    * Moved to `manipulate_matrix(matrix, vector, x) -> matrix`
* Constructing the solutions
    * Moved to `make_solutions(matrix, vector, x) -> solved`

### Complexity change

The cyclomatic complexity was 21 before the refactoring, and 9 after. So CC was reduced by 57%.