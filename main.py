"""
Wordle Solver using Information Theory (Entropy)

Student_1: Adham Hamdy Mohamed Mohamed  ID: 24010094
Student_2: Anas Alaa Abdo               ID: 24010004
CSED28++
"""

import json
import math
import heapq


# -----------------------------------------------------------------------------
#                             Functions' Definition
# -----------------------------------------------------------------------------
def get_pattern(guess: str, target: str) -> int:
    """
    A function to obtain the pattern for a word in the target with another word
    from the dictionary.

    Args:
        guess (str): a word from dictionary file.
        target (str): a word from target file.

    Returns:
        the pattern of the two words in decimal form.
    """

    total = 0
    letters = [0] * 26
    a = ord("a")

    for ch in target:
        letters[ord(ch) - a] += 1

    # greens
    for i in range(5):
        g = guess[i]
        t = target[i]

        if g == t:
            power = 4 - i
            total += (3**power) * 2
            letters[ord(g) - a] -= 1

    # yellows
    for i in range(5):
        g = guess[i]
        t = target[i]
        char_index = ord(g) - a

        if g != t and letters[char_index] > 0:
            power = 4 - i
            total += 3**power
            letters[char_index] -= 1

    return total


def feedback(
    dictionary_list: list[str],
    targets_list: list[str]
) -> list[list[int]]:
    """
    A function used to create an array containing the feedback for each two
    words.

    Args:
        dictionary_list (list[str]): a list of all words exist in the
        dictionary file.
        targets_list (list[str]): a list of all words exist in the targets
        file.

    Returns:
        a 2D array containing the feedbacks for each two words.
    """

    DIC_SIZE = len(dictionary_list)
    TARGET_SIZE = len(targets_list)
    M = [[0] * TARGET_SIZE for _ in range(DIC_SIZE)]

    for i in range(DIC_SIZE):
        for j in range(TARGET_SIZE):
            M[i][j] = get_pattern(dictionary_list[i], targets_list[j])

    return M


def filter_targets(
    guess_index: int,
    actual_pattern_str: str,
    remaining_targets: list[int],
    M: list[list[int]],
) -> list[int]:
    """
    A function used to filter targets after user input.

    Args:
        guess_index (int):
        actual_pattern_str (str): user's feedback in characters form.
        remaining_targets (list[int]): a list containing the remaining targets
        from the previous round.
        M (list[list[int]]): a 2D array containing the feedbacks for each two
        words.

    Returns:
        a list of the remaining targets after filtering.
    """

    actual_code = pattern_to_code(actual_pattern_str)
    new_targets = []

    for target_idx in remaining_targets:
        if M[guess_index][target_idx] == actual_code:
            new_targets.append(target_idx)

    return new_targets


def top_dictionary_words(
    remaining_targets: list[int],
    dictionary_list: list[str],
    dict_index: dict[str, int],
    M: list[list[int]],
    k: int,
) -> list[tuple[float, str]]:
    """
    A function used to display the top predicted word(s).

    Args:
    remaining_targets (list[int]):
    dictionary_list (list[str]): a list of all words exist in the dictionary
    file.
    dict_index (dict[str, int]): a dictionary of dictionary words and their
    indices.
    M (list[list[int]]): a 2D array containing the feedbacks for each two
    words.
    k (int): number of guesses to be displayed.

    Returns:
        a sorted list of tuples contains the top remaining guesses and their
        entropy.
    """
    top = []
    for word in dictionary_list:
        guess_index = dict_index[word]
        H = calculate_entropy(guess_index, remaining_targets, M)
        top.append((H, word))

    return heapq.nlargest(min(k, len(top)), top, key=lambda x: x[0])


def calculate_entropy(
    guess_index: int, remaining_targets: list[int], M: list[list[int]]
) -> float:
    """


    Args:
        guess_index (int):
        remaining_targets (list[int]):
        M (list[list[int]]): a 2D array containing the feedbacks for each two
        words.

    Returns:
        the entropy for a word.
    """

    TOTAL_PATTERNS = 243  # 3^5 possible feedback patterns
    branches = [0] * TOTAL_PATTERNS
    TOTAL_CANDIDATES = len(remaining_targets)
    entropy = 0.0

    for target_idx in remaining_targets:
        pattern = M[guess_index][target_idx]
        branches[pattern] += 1

    for count in branches:
        if count > 0:
            p = count / TOTAL_CANDIDATES
            entropy -= p * math.log2(p)

    return entropy


def pattern_to_code(pattern_str: str) -> int:
    """
    A function to convert the pattern from letters to decimal.

    Args:
        pattern_str (str): feedback in characters form.

    Returns:
        feedback in decimal form.
    """

    total = 0

    for i in range(5):
        power = 4 - i

        if pattern_str[i] == "g":
            total += (3**power) * 2

        elif pattern_str[i] == "y":
            total += 3**power

    return total


def code_to_pattern(code: int) -> str:
    """
    A function to convert the pattern from decimal to letters.

    Args:
        code (int): feedback in decimal form.


    Returns:
        feedback in characters form.
    """

    pattern = ""

    for _ in range(5):
        bit = code % 3

        if bit == 2:
            pattern += "g"

        elif bit == 1:
            pattern += "y"

        else:
            pattern += "r"

        code //= 3

    pattern = pattern[::-1]

    return pattern


# -----------------------------------------------------------------------------
#                                Load Files
# -----------------------------------------------------------------------------
with open("dictionary_5_letter.json") as f:
    dictionary_list = json.load(f)

with open("targets_5_letter.json") as f:
    targets_list = json.load(f)

dict_index = {word: i for i, word in enumerate(dictionary_list)}
target_index = {word: j for j, word in enumerate(targets_list)}


# -----------------------------------------------------------------------------
#                                Main Program
# -----------------------------------------------------------------------------
def main():
    remaining_targets = list(range(len(targets_list)))
    M = feedback(dictionary_list, targets_list)

    print("Welcome to Wordle Solver!")

    while True:
        # Ask the user to choose whether to display the top 15 predicted words
        # or just the top word.
        mode = input("Show top (1) guess or (15) guesses? Enter 1 or 15: ")

        if mode in ["1", "15"]:
            k = int(mode)
            break

        else:
            print("Invalid choice. Please enter 1 or 15.")

    round_num = 1

    while True:
        print(f"\n====== Round {round_num} ======")

        if len(remaining_targets) == 0:
            print("No targets left! Your feedback may be inconsistent.")
            break

        # Display the correct answer
        if len(remaining_targets) == 1:
            print("Answer is:", targets_list[remaining_targets[0]])
            break

        top_words = top_dictionary_words(
            remaining_targets, dictionary_list, dict_index, M, k
        )
        e, w = top_words[0]
        best_word = w

        print(f"Remaining possible answers: {len(remaining_targets)}")

        print(f"\nInformation Gain Reporting for best guess ({best_word}):")

        H_W = math.log2(len(remaining_targets))
        H_Y = e
        print(f"prior entropy H(W) = {H_W:.6f} bits")
        print(f"best-guess expected feedback entropy H(Y) = {H_Y:.6f}")
        print(f"expected posterior entropy H(W|Y) = {H_W - H_Y:.6f}")
        print(f"information gain I(W;Y) = {H_Y:.6f}")

        # Display the top predicted words each with its entropy
        print(f"\nTop {k} dictionary suggestions by entropy:")

        if k == 1:
            print(f"\nBest guess: {w}   entropy = {e:.6f}")

        else:
            for rank, (e, w) in enumerate(top_words, start=1):
                print(f"{rank:2d}. {w}   entropy = {e:.6f}")
            print(f"\nBEST = {best_word}")

        while True:
            # Prompt the user to enter the word they entered.
            guess = input("\nEnter your guess: ")

            if not (
                len(guess) == 5
                and guess.isalpha()
                and guess.islower()
                and guess in dict_index
            ):
                print(
                    "Invalid Input! Please Try again."
                    + "(must be 5 lowercase letters and in dictionary)"
                )

            else:
                break

        while True:
            # Ask the user to enter the feedback they obtain.
            pattern_str = input("Enter feedback (g/y/r): ")

            if not (
                len(pattern_str) == 5
                and all(c in "gyr" for c in pattern_str)
            ):
                print("Invalid Input! Please Try again.")

            else:
                break

        guess_index = dict_index[guess]
        remaining_targets = filter_targets(
            guess_index, pattern_str, remaining_targets, M
        )
        round_num += 1


if __name__ == "__main__":
    main()
