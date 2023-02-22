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
* bidirectional_dij
Maegan Chen Peralta
   * The purpose of the function is to find the length of the shortest path by conducting 2 searches, a forward search from the source and a reverse search from the destination
* next_term
Maegan Chen Peralta
   * The purpose of the function is to find the difference between the start term and the end term of the array and to find the number of terms jumped 

4. Are exceptions taken into account in the given measurements?
   
   No, neither the manual count or the automated tool takes exceptions into account.
    It's also worth noting that some of the functions like remove and _insert_repair don't have any exceptions
5. Is the documentation clear w.r.t. all the possible outcomes?
    
   Yes, the documentation is clear and describes all possible outcomes.

### Manual CC calculations

#### **inverse_of_matrix**

*Jennifer Larsson*

The function `inverse_of_matrix` has:

* 2 `if` statements
* 1 `elif` statement
* 5 `and` conditions
* 8 `for` loops
* 2 `return` statements

which gives a CC of `2 + 1 + 5 + 8 + 2 * 2 = 20`.

#### **Function 2**

#### **Function 3**

#### **Function 4**

## Refactoring

### polynom_for_points

*Jennifer Larsson*

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
Karlis Velins
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

### bidirectional_dij
Maegan Chen Peralta

Plan for refactoring complex code:
* Since there are duplicated code patterns, such as the following pairs of code: 
   * in lines 74-85 and 88-100, and
   * in lines 54-62 and 64-71, 
   we can limit these duplicates by extracting the common bits of code to helper functions. This will also help to improve code readability. 

Estimated impact of refactoring (lower CC, but other drawbacks?).
* The CC is expected to be lowered and readability should improve. However, two possible drawbacks are that firstly, the length of the code is increased. Secondly, someone reading the code would have to jump between functions when analysing the code as it has been broken down from a large chunk of code. Thankfully, these drawbacks are not major.

Carried out refactoring (optional, P+):

git diff ...

### Convert 
Michaela Mattsson
a smart way to reduce CC is to divide the function into smaller functions. An example of that for the Convert function is for example
* helper function to get the digit at a given place value
* helper function to get the word representation of a number less than 100
* helper function to get the word representation of a number
* helper function to convert a number to words

Although the CC would likely decrease, dividing the problem may not necessarily simplify understanding. However, using descriptive function names could make the code slightly easier to follow

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

*Jennifer Larsson*

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

Karlis Velins
Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements. https://github.com/KarlisKV/Coverage_algorithms/blob/17-improve-coverage/data_structures/binary_tree/red_black_tree.py

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

#### **Solution**
Michaela Mattsson
DIY coverage tool can be found [here](https://github.com/KarlisKV/Coverage_algorithms/blob/complex_func_solution/project_euler/problem_049/sol1.py)

* DIY tool does not take into account ternary operators
* DIY tool only cover if/ else statement and for/ while loops
* DIY tool measured a branch coverage of 100% and the automatic tool measure a coverage on 99%, which is more or less identical answer

#### **bidirectional_dij**
Maegan Chen Peralta
Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

### Evaluation

#### **polynom_for_points**

*Jennifer Larsson*

1. How detailed is your coverage measurement?

   The coverage measurement gives information about which branches are covered or not, and calculates the percentage. It does not provide more detailed information than that.

2. What are the limitations of your own tool?

   The tool is limited by not taking ternary operations into account. Furthermore, it is not modular - if new branches are added to the code, the tool will not take these into account unless modifying the tool.

3. Are the results of your tool consistent with existing coverage tools?

   The DIY tool measured a lower coverage than the automated tool (83% vs 93%), because it does not take all branch types into account.

#### **_insert_repair**
Karlis Velins
1. How detailed is your coverage measurement?

It checks for all if, elif else statements in the function, since those are the only ones that appear for this specific function 

2. What are the limitations of your own tool?

The tool requires manual input which makes it very error-prone. For a more complex function it is also not very efficient and takes a lot of work.

3. Are the results of your tool consistent with existing coverage tools?

I counted 16 branches but as I undestand the CC is the nr. of branches + 1 which is 17 so that matches the 17 that the automated lizard tool produced. For coverage I got 87.5% 
and the overall class got 79% coverage since it had other methods. My manual tool got a coverage for the existing tests for 87.5% 

#### **bidirectional_dij**
Maegan Chen Peralta

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

#### **Solution**
Michaela Mattsson
1. How detailed is your coverage measurement?

it only checks which branches were taken  and print out the percentage result of these

2. What are the limitations of your own tool?


it is very simple and and hard-coded which makes it naive for extending the function

3. Are the results of your tool consistent with existing coverage tools?

Yes,tool measured a branch coverage of 100% and the automatic tool measure a coverage on 99%

## Coverage improvement

### polynom_for_points

*Jennifer Larsson*

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
Karlis Velins
Show the comments that describe the requirements for the coverage.
https://github.com/KarlisKV/Coverage_algorithms/blob/17-improve-coverage/data_structures/binary_tree/red_black_tree.py
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


### bidirectional_dij
Maegan Chen Peralta

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link](https://github.com/KarlisKV/Coverage_algorithms/blob/master/web_programming/convert_number_to_words.py)
Original coverage: 79%

Report of new coverage: [link](https://github.com/KarlisKV/Coverage_algorithms/blob/coverage-improvement-convert-num/web_programming/convert_number_to_words.py)
New coverage: 98% 
Test cases added: line 9-21 se [here](https://github.com/KarlisKV/Coverage_algorithms/blob/coverage-improvement-convert-num/web_programming/convert_number_to_words.py)

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

### Convert 4
Michaela Matsson
Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

## Self-assessment: Way of working

1. Current state according to the Essence standard: 

   We are currently in the state *in use* according to the Essence standard. The principles and the foundation for the project have been established, and all group members are doing the required work. The practices and tools are being used in way that's appropriate for our project. However, we are using these tools in different ways and have not really established a common standard. For example, we have different practices for commit messages and branch naming. Furthermore, we have not taken the time to reflect upon our way of working until now, which would be good to do more often in order to reach the next state.

   The Essence way-of-working checklist can be found [here](https://docs.google.com/document/d/1R_0vUgGhzLNsjyxDPkSuWPGTFEUH8FV4r0b6I9HtQkE/edit?usp=sharing).

2. Was the self-assessment unanimous? Any doubts about certain items?

   Yes, all group members agreed on which criterias the group fulfilled in the Essence checklist.

3. How have you improved so far?

   The group was formed and we all got in contact with each other. After that, we agreed on our meeting structure, how the work should be divided and which tools/languages/practices we should use. So we have established our way-of-working and everyone is making progress on the lab. However, since this is the first project in the new group, we have not had time to reflect and update our way-of-working. So there are more improvements to make.

4. Where is potential for improvement?

   We have established our meeting structure, however our communication is not perfect yet. So there is potential for improving how we communicate and give feedback to each other, as the work so far has been quite individual. Another aspect we could work on is the team chemistry, as we only have meetings online and it's difficult to get to know each other over a screen. We could also work on establishing a mutual way of using our tools, such as Github, so that everyone in the group uses the tool in the same way.

## Overall experience

What are your main take-aways from this project? What did you learn?
In this project, we have learned 
* How to use automated coverage tool as well as building our own
* Why complexity and coverage is important and how to practically deal with these concepts
* How to calculate the cyclomatic complexity of a function
* How to enhance a test suite in order to get better coverage.
* How to refactor a function in order to decrease the cyclomatic complexity.

Is there something special you want to mention here?

One of our group members, Olivia Aronsson, was not able to participate in the project, so we are only four members.

## Statement of contributions

* Michaela Mattsson:
   * Manual complexity measurement for `Solution`
   * DIY coverage measurement for `Solution`
   * Two new test cases for `Convert`
   * Plan for refactoring `Convert`
   * Going for P
* Maegan Peralta:
   * Manual complexity measurement for `bidirectional_dij`
   * DIY coverage measurement for `bidirectional_dij`
   * Two new test cases for `bidirectional_dij`
   * Plan for refactoring `bidirectional_dij`
   * Going for P
* Karlis Kristofers Velins:
    * DIY coverage measurement for _insert_repair
    * Two new test cases for _insert_repair
    * Plan for refactoring _insert_repair
    * Going for P
* Jennifer Larsson: 
   * Manual complexity measurement for `inverse_of_matrix`
   * DIY coverage measurement for `polynom_for_points`
   * Four new test cases for `polynom_for_points`
   * Refactoring `polynom_for_points`
   * Going for P+, should meet requirements 1, 2 and 3
      1. Added four new test cases
      2. Used systematic commit messages and issues
      3. Refactored a function and decreased CC by more than 35%.
