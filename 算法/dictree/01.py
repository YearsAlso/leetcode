class TrieNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = {}


class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tops = {}
        self.words = []
    
    def insert(self, word):
        """
        Inserts a word into the trie.
        :type word: str
        :rtype: void
        """
        prev = None
        for i, s in enumerate(word):
            node = TrieNode(s, word[:i + 1])
            if i == 0:
                if self.tops.get(s,None) == None:
                    self.tops[s] = node
                    prev = node
                elif not s in self.tops:
                    return
                else:
                    prev = self.tops[s]
                continue
            
            if prev.next.get(s):
                prev = prev.next[s]
            else:
                prev.next[s] = node
                prev = node
        self.words.append(word)
    
    def search(self, word):
        """
        Returns if the word is in the trie.
        :type word: str
        :rtype: bool
        """
        if len(self.words) == 0:
            return False
        if not word[0] in self.tops:
            return False
        prev = self.tops[word[0]]
        for s in word[1:]:
            if prev.next.get(s):
                prev = prev.next[s]
            else:
                return False
        
        return True if len(prev.next) == 0 or word in self.words else False
    
    def startsWith(self, prefix):
        """
        Returns if there is any word in the trie that starts with the given prefix.
        :type prefix: str
        :rtype: bool
        """
        if len(self.words) == 0:
            return False
        if not prefix[0] in self.tops:
            return False
        prev = self.tops[prefix[0]]
        for s in prefix[1:]:
            if prev.next.get(s):
                prev = prev.next[s]
            else:
                return False
        return True
        

# Your Trie object will be instantiated and called as such:
# obj = Trie()
# obj.insert(word)
# param_2 = obj.search(word)
# param_3 = obj.startsWith(prefix)

def main():
    trie = Trie()
   # ["Trie", "insert", "insert", "insert", "insert", "insert", "insert", "search", "search", "search", "search",
   #  "search", "search", "search", "search", "search", "startsWith", "startsWith", "startsWith", "startsWith",
   #  "startsWith", "startsWith", "startsWith", "startsWith", "startsWith"]
   # [[],      ["app"], ["apple"], ["beer"], ["add"], ["jam"], ["rental"], ["apps"], ["app"], ["ad"], ["applepie"],
   # ["rest"], ["jan"], ["rent"], ["beer"],   ["jam"],     ["apps"],     ["app"],    ["ad"],      ["applepie"],
   # ["rest"],         ["jan"],    ["rent"],      ["beer"],      ["jam"]]
    print(trie.insert("app"))
    print(trie.insert("apple"))
    print(trie.insert("beer"))
    print(trie.insert("add"))
    print(trie.insert("jam"))
    print(trie.insert("rental"))
    print(trie.search("apps"))
    print(trie.search("app"))
    print(trie.search("search"))
    print(trie.search("ad"))
    print(trie.search("applepie"))
    print(trie.search("rest"))
    print(trie.search("jan"))
    print(trie.search("rent"))
    print(trie.search("beer"))
    print(trie.search("jam"))
    print(trie.startsWith("apps"))
    print(trie.startsWith("app"))
    print(trie.startsWith("ad"))
    print(trie.startsWith("applepie"))
    print(trie.startsWith("rest"))
    print(trie.startsWith("jan"))
    print(trie.startsWith("rent"))
    print(trie.startsWith("beer"))
    print(trie.startsWith("jam"))

if __name__ == '__main__':
    main()