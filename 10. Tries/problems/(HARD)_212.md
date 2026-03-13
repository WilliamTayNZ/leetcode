## Takeaways

- In trie + DFS problems, try to carry the current trie node in recursion rather than rebuilding prefixes.

- Storing the full word at terminal nodes can remove the need for a path list and string reconstruction.
  - This is instead of the usual "isEndOfWord"

- Problem-specific pruning during DFS unwinding can be lighter than implementing a full generic remove(word).

- A solution can have acceptable runtime but still poor memory usage because of temporary structures and repeated string creation.
