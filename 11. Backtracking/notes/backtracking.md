Use when:

- Combinations, permutations, etc
- Building up a partial solution
- ## Want all possible solutions
- Need to discard bad paths early
  - You are given a grid, board, set of digits, or string, and asked to form, build, place, or explore

Note: it's pretty slow so you generally only want to use it if you need to generate all solutions to something.

## Videos

https://youtu.be/Z_c4byLrNBU?t=3901

https://www.youtube.com/watch?v=p9m2LHBW81M

https://www.youtube.com/watch?v=Zq4upTEaQyM

## Template

1. Base Case
2. Choices
3. Constraints
4. Backtracking Step

```python
result = []

def dfs(start_index, path):
    if base_case_condition:
        save_result
        return

    for choice in choices:
        if violates_constraints:
            continue

        make_choice
        backtrack(updated_params)
        undo_choice  # Backtracking Step
```
