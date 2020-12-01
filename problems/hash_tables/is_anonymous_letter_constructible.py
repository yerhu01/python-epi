import collections

from test_framework import generic_test

# Time: O(n + m) where n and m are # of chars in letter and
#       magazine respectively
# Space: O(L) where L is # of distinct chars in letter
# Note: if characters coded in ASCII, could use 256 entry array instead of
# hash table
def is_letter_constructible_from_magazine(letter_text: str,
                                          magazine_text: str) -> bool:
    letter_char_freq = collections.Counter(letter_text)
    for c in magazine_text:
        if c in letter_char_freq:
            letter_char_freq[c] -= 1
            if letter_char_freq[c] == 0:
                del letter_char_freq[c]
                if not letter_char_freq:
                    return True
    return not letter_char_freq

# Brute force:
# For each character, count # in letter an magazine text.

# Pythonic solution that exploits collections.Counter. Note that the
# subtraction only keeps keys with positive counts.
def is_letter_constructible_from_magazine_pythonic(letter_text: str,
                                                   magazine_text: str) -> bool:
    return (not collections.Counter(letter_text) -
            collections.Counter(magazine_text))


if __name__ == '__main__':
    exit(
        generic_test.generic_test_main(
            'is_anonymous_letter_constructible.py',
            'is_anonymous_letter_constructible.tsv',
            is_letter_constructible_from_magazine))
