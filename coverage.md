### Coverage

## polynom_for_points

### DIY coverage measurement
1. The DIY coverage tool does no take ternary operators into account, but it does account for raising errors.
2. The DIY coverage tool is limited to if/else statements and while/for loops, but cannot take more complicated branching into account, for example ternary operators, which could cause unreliable results. 
3. The DIY coverage tool measuread a branch coverage of 83.3%, while the automated tool measuread branch coverage of 90 %. So the results were in the same range, but not exactly the same.