# Report for assignment 3 Group 28

This is a template for your report. You are free to modify it as needed.
It is not required to use markdown for your report either, but the report
has to be delivered in a standard, cross-platform format.

## Project

Name: The algorithms Python

URL: https://github.com/TheAlgorithms/Python

One or two sentences describing it:

The project is a collection of python algorithms. 

## Onboarding experience

Did it build and run as documented?
    
See the assignment for details; if everything works out of the box,
there is no need to write much here. If the first project(s) you picked
ended up being unsuitable, you can describe the "onboarding experience"
for each project, along with reason(s) why you changed to a different one.

Yes, the project ran as documented without problems.


## Complexity

1. What are your results for ten complex functions?

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
| 10 | ./data_structures/binary_tree/red_black_tree.py:123 | _insert_repair | 17 |
   
   * Did all methods (tools vs. manual count) get the same result?
      * The functions inverse_of_matrix got the same result with the automated tool and the manual count.
      * The function solution and _insert_repair did not get the same result with the automated tool and the manual count, with a difference of 1 CC.
      * the function remove had a CC of 21 instead of 19 by manual count
   * Are the results clear?
      * Yes, the results are clear.

2. Are the functions just complex, or also long?
* The function insert_repair is just complex, but quite short. This is since it is also recursive and acts also as a helper function to the insert function, the same can be said for the function remove since these 2  functions are just a part of a class
* The functions solution and inverse_of_matrix are both complex and long.

3. What is the purpose of the functions?
* inverse_of_matrix
   * The purpose of the function is to get the inverse of a 2x2 or 3x3 matrix.
* insert_repair
   * The purpose of the functions is to balance out the tree when a new node is inserted.
* remove
  * The purpose of this function is to be able to remove a node from the red-black tree correctly
* solution
   * The function is to find a 12-digit number that meets two conditions: 
      1. It is an arithmetic sequence of three prime numbers. 
      2. Each of the three 4-digit numbers is a permutation of each other.

4. Are exceptions taken into account in the given measurements?
   
   No, neither the manual count or the automated tool takes exceptions into account.
    It's also worth noting that some of the functions like remove and _insert_repair don't have any exceptions
5. Is the documentation clear w.r.t. all the possible outcomes?
    
   Yes, the documentation is clear and describes all possible outcomes.

## Refactoring

### polynom_for_points

Plan for refactoring complex code:

In order to decrease the complexity, the function can be split into smaller subfunctions.
There are four areas of the code with high complexity, that could be moved outside the function to helper functions. These areas are:
* Adding the x and x to the power of values to a matrix.
* Adding the y values to a vector.
* Manipulation the matrix.
* Constructing the solutions

Estimated impact of refactoring (lower CC, but other drawbacks?).

The refactoring should decrease the cyclomatic complexity and the length of the function. Otherwise, there would not be any impact on the code.

Carried out refactoring (optional, P+):

Four helper functions was added to decrease the CC of the code, one for each of the areas listed above. 
* Adding the x and x to the power of values to a matrix.
    * Moved to `add_x_values(coordinates, x) -> matrix`
* Adding the y values to a vector.
    * Moved to `add_y_values(coordinates, x) -> vector`
* Manipulation the matrix.
    * Moved to `manipulate_matrix(matrix, vector, x) -> matrix`
* Constructing the solutions
    * Moved to `make_solutions(matrix, vector, x) -> solved`

The refactoring can be found [here](https://github.com/KarlisKV/Coverage_algorithms/blob/8-refactor-polynom_for_points/linear_algebra/src/polynom_for_points.py) on lines: 1-96

The refactoring decreased the CC from 21 to 9, which gives a 57% decrease.

### _insert_repair

Plan for refactoring complex code:

* Combining the first two if statements with an elif.

* Using Boolean logic to combine several conditional statements and reduce the number of branches.

* *Reassigning self to the left or right child after rotating, if necessary. This avoids redundant code for the left and right cases.

* Assigning colors to multiple nodes in a single line, using tuple unpacking.

Estimated impact of refactoring (lower CC, but other drawbacks?).

This will reduce the cc but the issue is that the code will be way harder to read. Right now it is already difficult and it doesn't make sense to split the conditions amongst the various functions
to reduce complexity, it just is a very complex binary tree operation that needs these branches everywhere. Also adding these changes would make the code more error-prone.

Carried out refactoring (optional, P+):

git diff ...

### Function 3

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

### Function 4

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

## Coverage

### Tools

Document your experience in using a "new"/different coverage tool.

How well was the tool documented? Was it possible/easy/difficult to
integrate it with your build environment?

We used coverage.py as a coverage tool since we used Python as our coding language and it was the one that was recommended.
It was easy to use on our project, and was easy to understand and properly documented.

### Your own coverage tool

#### **polynom_for_points** 

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

The DIY coverage tool can be found [here](https://github.com/KarlisKV/Coverage_algorithms/blob/6-manual-coverage-measurement-for-polynom_for_points/linear_algebra/src/polynom_for_points.py)

What kinds of constructs does your tool support, and how accurate is
its output?

* The DIY coverage tool supports if/else statements and for/while loops, but *not* ternary operators
* The DIY coverage tool measuread a branch coverage of 83.3%, while the automated tool measuread branch coverage of 93 %. So the results were in the same range, but not exactly the same.

#### **_insert_repair**

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

#### **Function 3**
Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

#### **Function 4**
Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

#### **polynom_for_points**

1. How detailed is your coverage measurement?

   The coverage measurement gives information about which branches are covered or not, and calculates the percentage. It does not provide more detailed information than that.

2. What are the limitations of your own tool?

   The tool is limited by not taking ternary operations into account. Furthermore, it is not modular - if new branches are added to the code, the tool will not take these into account unless modifying the tool.

3. Are the results of your tool consistent with existing coverage tools?

   The DIY tool measured a lower coverage than the automated tool (83% vs 93%), because it does not take all branch types into account.

#### **_insert_repair**

1. How detailed is your coverage measurement?

It checks for all if, elif else statements in the function, since those are the only ones that appear for this specific function 

2. What are the limitations of your own tool?

The tool requires manual input which makes it very error-prone. For a more complex function it is also not very efficient and takes a lot of work.

3. Are the results of your tool consistent with existing coverage tools?

I counted 16 branches but as I undestand the CC is the nr. of branches + 1 which is 17 so that matches the 17 that the automated lizard tool produced. For coverage I got 87.5% 
and the overall class got 79% coverage since it had other methods. My manual tool got a coverage for the existing tests for 87.5% 
#### **Function 3**

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

#### **Function 4**

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

### polynom_for_points

Show the comments that describe the requirements for the coverage.

The requirements not met by the original test cases are:
* Branch 2:
   * Do not reach branch 0
   * The input satisfies: `len({tuple(pair) for pair in coordinates}) != len(coordinates)`
* Branch 4:
   * Do not reach branch 0 or 2
   * The input satisfies: `len(set_x) == 1`
* Branch 6:
   * Do not reach branch 0, 2 or 4
   * The input satisfies: `len(set_x) != len(coordinates)`
* Branch 20:
   * Do not reach branch 0, 2, 4 or 6
   * The input satisfies `len(remove_e) > 1`

Report of old / new coverage can be found [here](https://github.com/KarlisKV/Coverage_algorithms/blob/7-coverage-improvement-for-polynom_for_points/coverage_improvement.md)

Test cases added:

The added test cases can be found [here](https://github.com/KarlisKV/Coverage_algorithms/blob/7-coverage-improvement-for-polynom_for_points/linear_algebra/src/polynom_for_points.py) on lines 36-48. With these new test cases added, the requirements listed above are satisfied.

Number of test cases added: two per team member (P) or at least four (P+).

Four test cases were added (P+).

### _insert_repair

Show the comments that describe the requirements for the coverage.

Original coverage has it a 87.5% 

Report of old coverage: 

branch nr 0 True
branch nr 1 True
branch nr 2 True
branch nr 3 True
branch nr 4 False
branch nr 5 False
branch nr 6 True
branch nr 7 True
branch nr 8 True
branch nr 9 True
branch nr 10 True
branch nr 11 True
branch nr 12 True
branch nr 13 True
branch nr 14 True
branch nr 15 True
total coverage 87.5 %

Report of new coverage: New coverage has it at 100%

branch nr 0 True
branch nr 1 True
branch nr 2 True
branch nr 3 True
branch nr 4 True
branch nr 5 True
branch nr 6 True
branch nr 7 True
branch nr 8 True
branch nr 9 True
branch nr 10 True
branch nr 11 True
branch nr 12 True
branch nr 13 True
branch nr 14 True
branch nr 15 True
total coverage 100.0 %

Test cases added:

I added 2 test cases that 
1) Check whether condition 4 can be met without reaching condition 5
* This implies triggering a left-right rotation that makes the branches with set_flag(4) and set_flag(5) code to execute.
2) Check whether condition 4 and 5 can be met simultaneously
* This will call set_flag(4) when inserting 9 since it satisfies the condition if self.is_left() 
and self.parent.is_right(): in _insert_repair(), 
but it won't call set_flag(5) since there is no right child of 9.

I want to add here that whilst the coverage was 87.5% initially, it was since there were also insert_remove and delete tests
that overlapped with the insert test so when I removed those as you'll see in the branch, the coverage dropped to 62.5% which these 2 tests cover now without needing to add back the removed
previously written tests. 


### Function 3

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

### Function 4

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

1. Current state according to the Essence standard: 

   The group is currently in the state in place according to the Essence standard.

2. Was the self-assessment unanimous? Any doubts about certain items?

   Yes, the self-assesment was unanimous

3. How have you improved so far?

   The group was formed and its way of working was established. Since this is the first project in the new group, there has not been much improvement yet. 

4. Where is potential for improvement?

   The group could improve by working on their communication and team chemistry. 

## Overall experience

What are your main take-aways from this project? What did you learn?
In this project, we learned 
* how to use automated coverage tool as well as building our own
* why complexity and coverage is importand and how to deal with these concepts
* how to count the cyclomatic complexity

Is there something special you want to mention here?

One of our group members, Olivia Aronsson, was not able to participate in the project, so we are only four members.

## Statement of contributions

* Michaela Mattsson:
* Maegan Peralta:
* Karlis Kristofers Velins:
* Jennifer Larsson: 
   * Manual complexity measurement for `inverse_of_matrix`
   * DIY coverage measurement for `polynom_for_points`
   * Four new test cases for `polynom_for_points`
   * Refactoring `polynom_for_points`
   * Going for P+, should meet requirements 1, 2 and 3
      1. Added four new test cases
      2. Used systematic commit messages and issues
      3. Refactored a function and decreased CC by more than 35%.