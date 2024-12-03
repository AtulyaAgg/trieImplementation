class TrieNode:

    def __init__(self, data):
        self.children = [None]*26
        self.isEnd = False
        self.data = data
        if data != None:
            self.count = 1

class Trie:

    def __init__(self):
        self.root = TrieNode(None)

    def insert(self, word: str):
        curr = self.root

        for i in range(len(word)):
            index = ord(word[i])-ord('a')

            if curr.children[index] == None:
                curr.children[index] = TrieNode(word[i])
                curr = curr.children[index]
            else:
                curr = curr.children[index]
                curr.count += 1
        curr.isEnd = True

    def searchPrefix(self, word):
        res = ""
        curr = self.root
        for i in range(len(word)):
            index = ord(word[i]) - ord('a')

            if curr.children[index] is not None:
                curr = curr.children[index]
                if curr.count == 1:
                    res += curr.data
                    break
                else:
                    res += curr.data
        return res

    def search(self, word: str):
        curr = self.root

        for i in range(len(word)):
            index = ord(word[i]) - ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        if curr.isEnd and curr:
            return True
        return False

    def startsWith(self, prefix: str):
        curr = self.root

        for i in range(len(prefix)):
            index = ord(prefix[i])-ord('a')
            if curr.children[index] == None:
                return False
            curr = curr.children[index]
        return True

A = ["zebra", "dog", "duck", "dove"]
node = Trie()


res = []
for i in range(len(A)):
    node.insert(A[i])
for i in range(len(A)):
    res.append(node.searchPrefix(A[i]))
print(res)






