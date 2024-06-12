import json
import heapq
from trie import Trie


def get_words() -> json:
    f = open('common_words.json', 'r')

    with f as file:
        data = json.load(file)

    return data


class Controller:
    def __init__(self):
        self.trie = Trie()

        json_words = get_words()

        for word in json_words:
            self.trie.add_word(word)

    def get_result(self, search_text: str) -> list:
        search_text = search_text.lower()
        words_with_prefix = self.trie.search_prefix(search_text)

        return_data = []

        i = 0

        while i < 10 and i < len(words_with_prefix):
            word = words_with_prefix[i]
            return_data.append(word)
            i += 1

        if len(words_with_prefix) < 10:
            related_words = self.trie.search_related(search_text)
            heapq.heapify(related_words)

            while related_words and len(return_data) < 10:
                _, word = heapq.heappop(related_words)
                return_data.append(word)

        return return_data
