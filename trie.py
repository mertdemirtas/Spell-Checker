from trie_node import TrieNode
from levenshtein_distance import calculate_levenshtein_distance


class Trie:
    def __init__(self):
        self.root = TrieNode()

    def add_word(self, word):
        curr = self.root

        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]

        curr.end_of_word = True
        curr.actual_word = word

    def search_related(self, input_word: str) -> list:
        curr = self.root

        def dfs(node: TrieNode, search_word: list):
            if not node:
                return

            if node.end_of_word:
                levenshtein_dist = calculate_levenshtein_distance(input_word, ''.join(search_word))

                if len(search_word) >= len(input_word) and levenshtein_dist > 3:
                    return

                if levenshtein_dist != 0:
                    arr.append((levenshtein_dist, ''.join(search_word.copy())))

            for ch, sub_node in node.children.items():
                search_word.append(ch)
                dfs(sub_node, search_word)
                search_word.pop()

        arr = []
        dfs(curr, [])

        return arr

    def search_prefix(self, search_word) -> list:
        curr = self.root

        words_with_prefix = []

        for ch in search_word:
            if ch not in curr.children:
                return []
            curr = curr.children[ch]

        prefix_word = list(search_word)

        def dfs(node: TrieNode, completed_word: list):
            if not node:
                return

            if node.end_of_word:
                actual_word = ''.join(completed_word.copy())
                words_with_prefix.append(actual_word)

            for key, sub_node in node.children.items():
                completed_word.append(key)
                dfs(sub_node, completed_word)
                completed_word.pop()

        dfs(curr, prefix_word)

        return words_with_prefix
