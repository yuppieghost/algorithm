from collections import defaultdict


class TrieNode:
    def __init__(self):
        self.children = defaultdict(TrieNode)
        self.is_word = False


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, text: str) -> None:
        node = self.root
        for w in text:
            # defaultdict usage here
            node = node.children[w]
        node.is_word = True

    def find(self, pattern) -> bool:
        node = self.root
        for w in pattern:
            node = node.children.get(w)
            if not node:
                return False
        return node.is_word



if __name__ == "__main__":
    strs = ["how", "hi", "her", "hello", "so", "see"]
    trie = Trie()
    for s in strs:
        trie.insert(s)

    for s in strs:
        print(trie.find(s))

    print(trie.find("swift"))
