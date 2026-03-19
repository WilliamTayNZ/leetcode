# Dynamic Programming Notes

## What Dynamic Programming Is

Dynamic programming (DP) is an **algorithmic optimization technique** used when a problem can be broken into **smaller overlapping subproblems**, and the solutions to those subproblems can be reused to build the solution to the original problem.

At a high level, DP is about:

- breaking a problem into smaller parts
- solving those smaller parts
- avoiding repeated work
- combining those results to solve the full problem efficiently

---

## Why It Is Called “Dynamic Programming”

The term was coined by **Richard Bellman**.

- **Programming** here means **planning / decision-making**, not coding
- **Dynamic** refers to the changing nature of the states or decisions involved

The important ideas to remember are:

- **optimal decision-making**
- **solving subproblems**
- **reusing work**

---

## When a Problem Can Use Dynamic Programming

A problem is a good DP candidate when it has **both** of these properties.

### 1. Optimal Substructure

A problem has **optimal substructure** if the optimal solution to the whole problem can be built from optimal solutions to its subproblems.

#### Intuition

If solving the smaller pieces optimally helps you solve the big problem optimally, that is a strong DP sign.

---

### 2. Overlapping Subproblems

A problem has **overlapping subproblems** when the same subproblems are solved again and again.

#### Intuition

If recursion causes repeated function calls on the same inputs, DP can help by storing and reusing those answers.

---

## Fast Way to Recognize DP

When looking at a problem, ask:

1. Can I define it recursively?
2. Do I keep solving the same smaller cases more than once?
3. Can the final answer be built from smaller answers?

If yes, DP is likely useful.

A helpful mental workflow is:

- first try to describe the problem recursively
- then look for repeated subproblems
- if repeated work exists, DP can optimize it

---

## Common Indicators of DP Problems

### 1. Sequential Decision-Making

Many DP problems involve a sequence of decisions, where each choice affects future states.

---

### 2. Greedy-Like Structure / Local Choices Affect Future States

Some problems may seem greedy, but can also be solved with DP.

The key idea is that a locally good decision affects future possibilities, so you may need to track states carefully.

---

### 3. State Transitions

A DP problem often moves from one **state** to another, where the current answer depends on previous states.

A very common pattern is:

```text
dp[i] = built from earlier dp values
```

### 4. Paths, Arrays, or Reaching a State

Problems involving:

- finding an optimal path
- moving through a grid
- arranging elements
- reaching one state from another

often suggest DP.

---

### 5. Counting / Maximizing / Minimizing

DP frequently appears when the problem asks for:

- number of ways
- maximum value
- minimum value
- best / worst possible outcome

---

## General DP Workflow

A practical progression for solving DP problems is:

### Step 1: Write the Naive Recursive Solution

Start with the plain recursive definition, even if it is slow.

Why?

- it reveals the structure of the problem
- it helps identify base cases
- it exposes overlapping subproblems

This version may be very slow, such as exponential or factorial time, but that is okay at first.

---

### Step 2: Optimize with Top-Down DP (Memoization)

Take the recursive solution and add a **cache**.

This is called:

- **top-down DP**
- **memoization**

You still use recursion, but whenever you compute a result once, you store it so future calls can reuse it in constant time.

Common names for this storage:

- memo
- cache
- dictionary / hashmap

---

### Step 3: Convert to Bottom-Up DP (Tabulation)

Instead of recursion, build answers from the smallest subproblems upward using loops.

This is called:

- **bottom-up DP**
- **tabulation**

You usually fill a table / array like:

```text
dp[0], dp[1], dp[2], ...
```

Bottom-up DP often has the same asymptotic time complexity as top-down DP, but is often faster in practice because loops are generally cheaper than recursion.

---

### Step 4: Optimize Space if Possible

Sometimes you do not need the entire DP table.

If each state depends only on a few previous states, you may be able to replace the array with a few variables.

This can reduce space from `O(n)` to `O(1)`.

---

## Fibonacci as the Classic DP Example

Fibonacci is a classic example for understanding the DP progression because it clearly shows overlapping subproblems and how repeated work can be removed.

Sequence definition:

- `fib(0) = 0`
- `fib(1) = 1`
- `fib(n) = fib(n - 1) + fib(n - 2)` for `n > 1`

Sequence:

~~~text
0, 1, 1, 2, 3, 5, 8, ...
~~~

---

## 1. Naive Recursive Solution

The most direct implementation simply matches the recurrence:

~~~python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    return fib(n - 1) + fib(n - 2)
~~~

### Why it is slow

It repeatedly recomputes the same values.

This creates a recursion tree with lots of duplicated work.

### Complexity

- **Time:** approximately `O(2^n)`
- **Space:** `O(n)` due to recursion depth

---

## 2. Top-Down DP (Memoization)

### Core Idea

Store results the first time they are computed.

Then if the same subproblem appears again, just return the stored answer.

### Template

~~~python
def fib(n):
    memo = {0: 0, 1: 1}

    def f(x):
        if x in memo:
            return memo[x]
        memo[x] = f(x - 1) + f(x - 2)
        return memo[x]

    return f(n)
~~~

### Why it works

Each Fibonacci value is computed only once.

After that, repeated calls become constant-time lookups.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

The space is `O(n)` because of:

- the memo table
- the recursion stack

---

## 3. Bottom-Up DP (Tabulation)

### Core Idea

Build the answers iteratively from the base cases upward.

Instead of asking recursively for smaller values, explicitly fill a table.

### Template

~~~python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 0
    dp[1] = 1

    for i in range(2, n + 1):
        dp[i] = dp[i - 1] + dp[i - 2]

    return dp[n]
~~~

### Why `n + 1`

Because we want indices from `0` through `n` inclusive.

### Complexity

- **Time:** `O(n)`
- **Space:** `O(n)`

---

## 4. Bottom-Up with Constant Space

### Observation

To compute the next Fibonacci number, you only need the previous two.

So instead of storing the whole array, just keep two variables.

### Template

~~~python
def fib(n):
    if n == 0:
        return 0
    if n == 1:
        return 1

    prev = 0
    curr = 1

    for _ in range(2, n + 1):
        prev, curr = curr, prev + curr

    return curr
~~~

### Complexity

- **Time:** `O(n)`
- **Space:** `O(1)`

This is usually the best interview solution for Fibonacci.

---

## Top-Down vs Bottom-Up

### Top-Down (Memoization)

#### Characteristics

- uses recursion
- starts from the original problem and breaks downward
- stores results in a cache

#### Pros

- often easier to derive from the recurrence
- feels natural when you already understand the recursive definition

#### Cons

- recursion overhead
- possible stack depth issues
- often slightly slower in practice than bottom-up

---

### Bottom-Up (Tabulation)

#### Characteristics

- uses loops
- starts from the smallest base cases and builds upward
- fills a table / array iteratively

#### Pros

- avoids recursion
- often faster in practice
- no recursion stack overhead

#### Cons

- can feel less intuitive at first
- requires figuring out the correct iteration order

---

## Rule of Thumb

- If recursion is easy to write and reason about, start with **top-down**
- If you want the most efficient practical implementation, prefer **bottom-up**
- If only a few previous states matter, try **space optimization**

---

## How to Think About DP on a New Problem

### 1. Define the State

Ask:

- what does `dp[i]` mean?
- what does the function `f(i)` represent?

Examples of meanings:

- best answer up to index `i`
- number of ways to reach state `i`
- minimum cost to reach state `i`

---

### 2. Identify the Base Cases

What are the smallest cases whose answers are obvious?

These anchor the recurrence and let larger states build from them.

---

### 3. Write the Recurrence / Transition

How does the current state depend on earlier states?

Generic form:

~~~text
dp[current] = built from previous states
~~~

This is the heart of the DP solution.

---

### 4. Decide Top-Down or Bottom-Up

Ask:

- do I want to write recursion + memo?
- can I fill a table iteratively?

Both usually compute the same recurrence, just in different directions.

---

### 5. Check for Space Optimization

Do you really need the whole table?

If each state only depends on a constant number of previous states, reduce memory usage.

---

## Important Intuition

DP is not random memorization of tricks.

At its core, DP is about:

- recognizing repeated work
- defining subproblems clearly
- storing results so each subproblem is solved once
- building the full answer from those smaller results

---

## Quick Summary

### DP requires

- **optimal substructure**
- **overlapping subproblems**

### Main process

1. write recursive solution
2. add memoization
3. convert to bottom-up tabulation
4. optimize space if possible

### Fibonacci progression

- naive recursion: `O(2^n)` time
- top-down memoization: `O(n)` time, `O(n)` space
- bottom-up tabulation: `O(n)` time, `O(n)` space
- bottom-up constant space: `O(n)` time, `O(1)` space

---

## One-Line Mental Model

Dynamic programming = **solve smaller subproblems once, save their answers, and reuse them to build the final solution**.