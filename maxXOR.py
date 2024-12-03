class TrieNode:
    def __init__(self):
        self.children = {}

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, num):
        curr = self.root

        i=4
        while i>=0:
            bit = (num>>i)&1

            if bit not in curr.children:
                curr.children[bit] = TrieNode()
            curr = curr.children[bit]
            i-=1

    def max_xor_helper(self, value):
        curr = self.root
        curr_ans = 0

        i=4
        while i>=0:
            bit = (value>>i)&1
            if bit^1 in curr.children:
                curr = curr.children[bit^1]
                curr_ans = curr_ans + (1<<i)
            else:
                curr = curr.children[bit]
            i-=1
        return curr_ans

A = [5, 10]

node = Trie()
node.insert(A[0])
max_ans=0
for i in range(1, len(A)):
    max_ans = max(max_ans, node.max_xor_helper(A[i]))
 print(max_ans)