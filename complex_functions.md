# Ten most complex functions

| Nr | Path | Function | CC |
| -- | ---- | -------- | -- |
| 1 | ./data_structures/binary_tree/red_black_tree.py:212 |  _remove_repair | 31 |
| 2 | ./digital_image_processing/edge_detection/canny.py:21 | canny | 26 |
| 3 | ./linear_algebra/src/polynom_for_points.py:1 | points_to_polynomial | 21 |
| 4 | ./project_euler/problem_551/sol1.py:21 | next_term | 20 |
| 5 | ./project_euler/problem_049/sol1.py:95 | solution | 20 |
| 6 | ./graphs/bi_directional_dijkstra.py:20 | bidirectional_dij | 20 |
| 7 | ./graphs/a_star.py:12 | search | 20 |
| 8 | ./matrix/inverse_of_matrix.py:8: |  inverse_of_matrix | 20 |
| 9 | ./data_structures/binary_tree/red_black_tree.py:155 | remove | 19 |
| 10 | ./data_structures/heap/binomial_heap.py:131 | merge_heaps | 19 |

## inverse_of_matrix
1. The manual CC count resulted in 20 CC, same as the tool.
2. The function is 147 LOC, 84 is you do not count the comments.
3. The purpose of the function is to get the inverse of a 2x2 or 3x3 matrix. The CC is high because there are different sets of conditions that have to be met in order to inverse different matrix types.
4. The function raises value errors at three locations in the code, provided that the corresponding condition is met. Neither the tool nor the manual count took these into account when measuring the CC.
5. The documentation about the function is very clear about the different possible outcomes induced by different branches taken. There is example output for all possible branches.


## solution
1. manual CC count 19, tool CC count resulted in 20
2. function is 40 lines of code without comments and 55 with comments 
3. the function is to find a 12-digit number that meets two conditions: 1. It is an arithmetic sequence of three prime numbers. 2.Each of the three 4-digit numbers is a permutation of each other. cc is high because there are many requirements to take into account.
4. the functions does not raise any value errors.
5. the documentation of the function is lacking regarding the different possible outcomes
