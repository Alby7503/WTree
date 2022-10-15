"""WTree.py"""
from typing import Union

with open("words.txt", 'r', encoding="ascii") as words_file:
    words = words_file.read().splitlines()

MAX_INDEXED_LETTERS = 2

def index(word: str, position: int, current_index: dict) -> Union[dict, list]:
    """Index a word into the tree"""
    if position < len(word) and position < MAX_INDEXED_LETTERS:
        correct_dictionary = {} if word[position] not in current_index else current_index[word[position]]
        current_index[word[position]] = index(word, position + 1, correct_dictionary)
        return current_index
    if isinstance(current_index, list):
        current_index.append(word)
        return current_index
    return [word]


def print_tree(current_index) -> None:
    """Print an indexed tree formatted"""
    for branch in current_index:
        if type(current_index[branch]) == list:
            print(f"\t{current_index[branch]}", end='\n')
        else:
            print(f"{branch}", end='\n\t')
            print_tree(current_index[branch])


def search_tree(word: str, source) -> Union[None, dict]:
    """Search for a word in the tree"""
    position = 0
    try:
        while isinstance(source, dict):
            source = source[word[position]]
            position += 1
            if position == len(word):
                break
        return source
    except KeyError:
        return None


tree = {}
for iword in words:
    index(iword, 0, tree)
# print_tree(tree)
SEARCH_WORD = "re"
search_result = search_tree(SEARCH_WORD, tree)
if isinstance(search_result, dict):
    print(SEARCH_WORD)
    print_tree(search_result)
else:
    print(search_result)
