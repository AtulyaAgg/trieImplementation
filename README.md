# Trie Implementation in Python

## Overview

This repository contains a Python implementation of the Trie data structure, including methods for inserting words, searching for words, finding prefixes, and checking for prefix existence.

## Features

### TrieNode Class

- Represents each node in the Trie with:
    - ``` children: ``` A list of child nodes.
    - ``` isEnd: ``` A boolean indicating the end of a word.
    - ``` data: ``` The character stored at the node.
    - ``` count: ``` Tracks the frequency of the character.

## Trie Class

- Implements the Trie data structure with the following methods:
    - ``` insert(word: str): ``` Inserts a word into the Trie.
    - ``` search(word: str): ``` Checks if a word exists in the Trie.
    - ``` searchPrefix(word: str): ``` Finds the shortest unique prefix for a given word.
    - ``` startsWith(prefix: str): ``` Checks if any word in the Trie starts with a given prefix.

## Usage

```

# Example usage
A = ["zebra", "dog", "duck", "dove"]
node = Trie()

res = []
for word in A:
    node.insert(word)

for word in A:
    res.append(node.searchPrefix(word))

print(res)  # Output: ['z', 'dog', 'du', 'dov']

```

## How It Works

1. **Insertion:**
    - Words are inserted character by character.
    - New nodes are created as needed.
    - The count attribute tracks the number of times a character is visited during insertion.

2. **Search:**
    - Traverses the Trie to verify if a word exists.

3. **Prefix Search:**
    - Constructs the shortest unique prefix for a word by traversing the Trie until a node's count is 1.

4. **Prefix Check:**
    - Validates if any word in the Trie starts with a given prefix.

### Running the Script

Run the script directly:

```

python trie.py

```

The script processes an example list of words and prints their shortest unique prefixes.


### Example Output
For the ``` input ["zebra", "dog", "duck", "dove"], ``` the script outputs:

```

['z', 'dog', 'du', 'dov']

```

### Contributing

Contributions are welcome! 🙌
Feel free to open issues or submit pull requests for improvements.
