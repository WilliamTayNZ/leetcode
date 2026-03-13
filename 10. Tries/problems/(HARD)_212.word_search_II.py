# SOLUTION 1: OPTIMAL, STILL USES A LIGHT TRIE ABSTRACTION

class TrieNode:
    def __init__(self):
        self.children = {}
        self.word = None # Store the full word here instead of just a bool isEndOfWord, so we can directly append it to matchedWords when we find a word
        
class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def add(self, word):
        node = self.root
        for c in word:
            if c not in node.children:
                node.children[c] = TrieNode()
            node = node.children[c]

        # mark the existence of a word in trie node
        node.word = word

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        trie = Trie()

        for word in words:
            trie.add(word)

        m = len(board)
        n = len(board[0])

        matchedWords = []

        def dfs(r, c, parent):

            letter = board[r][c]
            currNode = parent.children[letter]

            # check if we find a match of word
            if currNode.word is not None:
                matchedWords.append(currNode.word)
                currNode.word = None

            # Before the EXPLORATION, mark the cell as visited
            board[r][c] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = r + rowOffset, c + colOffset
                if (
                    newRow < 0
                    or newRow >= m
                    or newCol < 0
                    or newCol >= n
                ):
                    continue
                if not board[newRow][newCol] in currNode.children:
                    continue
                dfs(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[r][c] = letter

            # Optimization: prune the matched leaf node the trie
            if not currNode.children and currNode.word is None:
                del parent.children[letter]

        for r in range(m):
            for c in range(n):
                # starting from each of the cells
                if board[r][c] in trie.root.children:
                    dfs(r, c, trie.root)

        return matchedWords
    


# SOLUTION 2: LEETCODE EDITORIAL, USES A DICT() AS THE TRIE 

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        WORD_KEY = "$"

        trie = {}
        for word in words:
            node = trie
            for letter in word:
                # retrieve the next node; If not found, create a empty node.
                node = node.setdefault(letter, {})
            # mark the existence of a word in trie node
            node[WORD_KEY] = word

        rowNum = len(board)
        colNum = len(board[0])

        matchedWords = []

        def backtracking(row, col, parent):

            letter = board[row][col]
            currNode = parent[letter]

            # check if we find a match of word
            word_match = currNode.pop(WORD_KEY, False)
            if word_match:
                # also we removed the matched word to avoid duplicates,
                #   as well as avoiding using set() for results.
                matchedWords.append(word_match)

            # Before the EXPLORATION, mark the cell as visited
            board[row][col] = "#"

            # Explore the neighbors in 4 directions, i.e. up, right, down, left
            for rowOffset, colOffset in [(-1, 0), (0, 1), (1, 0), (0, -1)]:
                newRow, newCol = row + rowOffset, col + colOffset
                if (
                    newRow < 0
                    or newRow >= rowNum
                    or newCol < 0
                    or newCol >= colNum
                ):
                    continue
                if not board[newRow][newCol] in currNode:
                    continue
                backtracking(newRow, newCol, currNode)

            # End of EXPLORATION, we restore the cell
            board[row][col] = letter

            # Optimization: incrementally remove the matched leaf node in Trie.
            if not currNode:
                parent.pop(letter)

        for row in range(rowNum):
            for col in range(colNum):
                # starting from each of the cells
                if board[row][col] in trie:
                    backtracking(row, col, trie)

        return matchedWords
    


# SOLUTION 3: MY ORIGINAL PAINSTAKING SOLUTION
 # Stores a lot of extra state, and hence is very space inefficient

class TrieNode:
    def __init__(self):
        self.children = {}
        self.isEndOfWord = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                curr.children[c] = TrieNode()
            curr = curr.children[c]
        curr.isEndOfWord = True
    
    # Used when we've already found a word
    # Important for efficiency, so our algorithm doesn't waste time finding a word it already previously found
    # Guaranteed to be called with a valid word
    def remove(self, word):
        curr = self.root

        trie_path = []

        # Find the end of the word first
        # Build a trie path as we go
        for c in word:
            curr = curr.children[c]
            trie_path.append(curr)

        # If the word is still a prefix of another word, just remove the endOfWord marker
        if curr.children:
            curr.isEndOfWord = False
        else: # If the word is not still a prefix of another word, we need to remove the word by going backwards. 

            # We want to access the parent of this last character to delete the connection from there

            # If the word is longer than 1 character, we can do it like this
            if len(trie_path) > 1:
                trie_index = len(trie_path) - 2
                parent = trie_path[trie_index]
                del parent.children[word[trie_index+1]]
            # Else if the word was only 1 character, delete it from the root and return
            else:
                del self.root.children[word[0]]
                return
                
            # Consider the parent our "current" node now
            # Iteratively, if this "current" node still has children, we stop the deletion process. Else, if it has no more children now, we can go to its parent and delete the connection.

            while trie_index > 0:
                if parent.children:
                    break
                else:
                    trie_index -= 1
                    parent = trie_path[trie_index]
                    del parent.children[word[trie_index + 1]]
            if not trie_path[trie_index].children:
                del self.root.children[word[0]]

        
    def searchWord(self, word):
        curr = self.root
        for c in word:
            if c not in curr.children:
                return False
            curr = curr.children[c]

        return curr.isEndOfWord
    
    def startsWith(self, prefix):
        curr = self.root
        for c in prefix:
            if c not in curr.children:
                return False
            curr = curr.children[c]
        return True

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        # BASIC APPROACH:

            # Iterate through each cell row-by-row to find possible starting characters of a desired word
            # We then want to explore adjacent cells, building the path until we can find one of our desired words

            # We can add all desired words to a trie
            
            # Then when we iterate through cells, we just search for our desired word in each cell, checking all 4 adjacent directions and backtracking from them


        # IMPORANT CONSTRAINTS/EDGE CASES:

            # A word can be a prefix of another word
              # Hence it is important to not kill a path just because we've found a word, as there could be another word to find by continuing on the path

            # The result cannot have duplicate words.

            # A cell cannot be used twice for a word. This means once we put a cell on our path we have to ensure it does not get used later in the path.

            # We only need to find a word once, so once found we should not look for it anymore

        def dfs(r, c):
            if board[r][c] == "S": # node is already used in path
                return

            path.append(board[r][c])

            prefix = ''.join(path)

            # If the prefix is not found, we kill this path
            if not trie.startsWith(prefix):
                path.pop()
                return

            temp = board[r][c]
            board[r][c] = "S" # marks that the node is being used in the path so it doesn't get reused

            # If we've found the word, add it to result
            if trie.searchWord(prefix):
                result.append(prefix)
                trie.remove(prefix)

            # Search the children for a word / further words
            if r > 0:
                dfs(r-1, c)
            if r < m-1:
                dfs(r+1, c)
            if c > 0:
                dfs(r, c-1)
            if c < n-1:
                dfs(r,c+1)

            path.pop()
            board[r][c] = temp


        trie = Trie()

        # Add all words to trie
        for word in words:
            trie.add(word)

        # As we build the word, we keep searching our word in the Trie
        path = []
        result = []
        m = len(board)
        n = len(board[0])

        for r in range(m):
            for c in range(n):
                dfs(r, c)

        return result