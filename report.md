# Report for assignment 3

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
| 10 | ./data_structures/heap/binomial_heap.py:131 | merge_heaps | 19 |
   
   * Did all methods (tools vs. manual count) get the same result?
      * The functions inverse_of_matrix and insert_repair got the same result with the automated tool and the manual count.
      * The function solution did not get the same result with the automated tool and the manual count, with a difference of 1 CC.
   * Are the results clear?
      * Yes, the results are clear.

2. Are the functions just complex, or also long?
* The function insert_repair is just complex, but quite short.
* The functions solution and inverse_of_matrix are both complex and long.

3. What is the purpose of the functions?
* inverse_of_matrix
   * The purpose of the function is to get the inverse of a 2x2 or 3x3 matrix.
* insert_repair
   * The purpose of the functions is to balance out the tree when a new node is inserted.
* solution
   * The function is to find a 12-digit number that meets two conditions: 
      1. It is an arithmetic sequence of three prime numbers. 
      2. Each of the three 4-digit numbers is a permutation of each other.

4. Are exceptions taken into account in the given measurements?
   
   No, neither the manual count or the automated tool takes exceptions into account.

5. Is the documentation clear w.r.t. all the possible outcomes?

   Yes, the documentation is clear and describes all possible outcomes.

## Refactoring

### Function 1

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

Carried out refactoring (optional, P+):

git diff ...

### Function 2

Plan for refactoring complex code:

Estimated impact of refactoring (lower CC, but other drawbacks?).

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

We used coverage.py as a coverage tool. It was easy to use on our project, and was easy to understand and properly documented.

### Your own coverage tool

#### **Function 1** 

Show a patch (or link to a branch) that shows the instrumented code to
gather coverage measurements.

The patch is probably too long to be copied here, so please add
the git command that is used to obtain the patch instead:

git diff ...

What kinds of constructs does your tool support, and how accurate is
its output?

#### **Function 2**

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

### Function 1

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

### Function 2

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

### Function 3

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

### Function 4

1. How detailed is your coverage measurement?

2. What are the limitations of your own tool?

3. Are the results of your tool consistent with existing coverage tools?

## Coverage improvement

### Function 1

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

### Function 2

Show the comments that describe the requirements for the coverage.

Report of old coverage: [link]

Report of new coverage: [link]

Test cases added:

git diff ...

Number of test cases added: two per team member (P) or at least four (P+).

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
