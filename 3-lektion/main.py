def letter_indicies(word):
    for i in range(len(word)):
        print(i, word[i])


def different_letters(word1, word2):
    for letter in word1:
        if letter not in word2:
            print(letter, end=" ")


def nested_sum(lists):
    total = 0
    for i in lists:
        if isinstance(i, list):
            total += nested_sum(i)
        else:
            total += i
    return total


def is_sorted(l):
    for i in range(len(l) - 1):
        if l[i] > l[i + 1]:
            return False
    return True


if __name__ == "__main__":
    # letter_indicies("hej")
    # different_letters("hejsdfsdf", "haj")
    print(nested_sum([[[1, 2], [1, 2]], [[1, 2], [1, 2]]]))
    print(is_sorted([1, 2, 3, 4, 5, 6, 7, 9, 8]))
