class CharacterNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class WordDictionary:

    def __init__(self):
        self.root = CharacterNode()

    
    # O(M) time where M is the key (word) length
      # At each step,  we either examine or create a node in the trie
    # O(M) space, in the worst case we need to add M new nodes
    def addWord(self, word: str) -> None:
        curr = self.root

        # For each character c in word, if c not in node's children, create a CharacterNode and dictionary value
        # Then set curr to curr.children[c]
        for c in word:
            if c not in curr.children:
                curr.children[c] = CharacterNode()
            curr = curr.children[c]

        curr.isEndOfWord = True

    # O(M) time for "well-defined" words (without dots)
    # O(N * 26^M) time for the "undefined" words (with dots) where N is number of keys
      # This would be for the worst-case where we search for a word liike ....D though in these test cases there are only at most 2 dots in a word

    # O(1) space for well-defined words, O(M) for undefined words (recursion stack)
    
    def search(self, word: str) -> bool:
        # When the character is a . we have to recursively search every child
        # Run a DFS through the remaining  characters and as long as one returns true, we return true

        def dfs(root, j):
            curr = root

            for i in range(j+1, len(word)):
                if word[i] == ".":
                    for childNode in curr.children.values():
                        if dfs(childNode, i):
                            return True
                    return False
                else:
                    if word[i] not in curr.children:
                        return False
                    curr = curr.children[word[i]]
            return curr.isEndOfWord

        return dfs(self.root, -1)



# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord(word)
# param_2 = obj.search(word)