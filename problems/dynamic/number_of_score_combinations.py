from typing import List

from test_framework import generic_test

# Time: O(sn) where s is the # of type of plays, and n is the final score
# Space: O(sn)
def num_combinations_for_final_score(final_score: int,
                                     individual_play_scores: List[int]) -> int:
    num_combinations = [[1] + [0]*final_score
                         for _ in range(len(individual_play_scores))]

    for i in range(len(individual_play_scores)):
        for j in range(1, final_score+1):
            without_play = (num_combinations[i-1][j] if i >= 1 else 0)
            with_play = (num_combinations[i][j-individual_play_scores[i]]
                            if j >= individual_play_scores[i] else 0)
            num_combinations[i][j] = without_play + with_play

    return num_combinations[-1][-1]

if __name__ == '__main__':
    exit(
        generic_test.generic_test_main('number_of_score_combinations.py',
                                       'number_of_score_combinations.tsv',
                                       num_combinations_for_final_score))
