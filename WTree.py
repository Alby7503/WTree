"""WTree.py"""
from typing import Union

with open("words.txt", 'r', encoding="ascii") as words_file:
    words = words_file.read().splitlines()

MAX_INDEXED_LETTERS = 4

def index(word: str, position: int, current_index: dict) -> Union[dict, list]:
    """Index a word into the tree"""
    if position < len(word) and position <= MAX_INDEXED_LETTERS:
        current_index[word[position]] = index(
            word, position + 1, current_index.get(word[position], {}))
        return current_index
    if isinstance(current_index, list):
        return current_index + [word]
    return [word]


def print_tree(current_index, previous: str = '') -> None:
    """Print an indexed tree formatted"""
    print('\t' * len(previous), end = '')
    for branch in current_index:
        if type(current_index[branch]) == list:
            print(f"\t{' '.join(current_index[branch])}", end='\n')
        else:
            print(f"({previous}){branch}", end='\n')
            print_tree(current_index[branch], previous + branch)


def search_tree(word: str, source) -> Union[None, dict]:
    """Search for a word in the tree"""
    position = 0
    try:
        word_length = len(word)
        while isinstance(source, dict) and position != word_length:
            source = source[word[position]]
            position += 1
        return source
    except KeyError:
        return None


tree = {}
for iword in words:
    index(iword, 0, tree)
#print_tree(tree)
SEARCH_WORD = "re"
search_result = search_tree(SEARCH_WORD, tree)
if isinstance(search_result, dict):
    print(f"Search results for '{SEARCH_WORD}':")
    print_tree(search_result, SEARCH_WORD)
else:
    print(search_result)
