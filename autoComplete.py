class TrieNode:
    def __init__(self):
        self.child = [None]*26
        # isEndOfWord is True if node represent the end of the word
        self.isend = False
        self.idx_ans = []

def insert(root, word, idx, W):
    temp = root
    for i in range(len(word)):
        chr_val = ord(word[i]) - 97
        if(temp.child[chr_val] == None):
            temp.child[chr_val] = TrieNode()
        temp = temp.child[chr_val]
        if(len(temp.idx_ans) < 5):
            temp.idx_ans.append([W[idx], idx])
    temp.isend = True

def query(root, prefix, W):
    temp = root
    ans = []
    for i in range(len(prefix)):
        chr_val = ord(prefix[i]) - 97
        if(temp.child[chr_val] == None):
            temp = temp.child[chr_val]
            break
        temp = temp.child[chr_val];
    if(temp == None):
        return ans
    return temp.idx_ans


def solve(A, W, B):
    root = TrieNode()
    v = []
    for i in range(len(A)):
        v.append([W[i], i])
    v.sort()
    print(v)
    for i in range(len(v)-1, -1, -1):
        insert(root, A[v[i][1]], v[i][1], W)
    for i in range(len(B)):
        ans = query(root, B[i], W)
        if(len(ans) == 0):
            print("-1", end = " ")
        else:
            for j in range(len(ans)):
                print(A[ans[j][1]], end = " ")
        print()

def main():
    # YOUR CODE GOES HERE
    # Please take input and print output to standard input/output (stdin/stdout)
    # E.g. 'input()/raw_input()' for input & 'print' for output
    # t = int(input())
    # for _ in range(t):
    #     n, m = input().split(" ")
    #     n = int(n)
    #     m = int(m)
    #     A = list(input().split(" "))
    #     W = list(map(int,input().split(" ")))
    #     B = list(input().split(" "))
    A = ['abcd', 'aecd', 'abaa', 'abef', 'acdcc', 'acbcc']
    W = [ 2, 1, 3, 4, 6, 5]
    B = ['ab', 'abc', 'a']
    solve(A, W, B)
if __name__ == '__main__':
    n = 4
    str = ""
    while n:
        if n&1:
            str += "1"
        else:
            str += "0"
        n = n>>1
    print(str[::-1])

