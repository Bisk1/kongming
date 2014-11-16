
def word_difference(word1, word2):
    """
    Determine how different are two words in the same language
    :param word1: first word to compare
    :param word2: second word to compare
    :return: number of different characters or 1000 if more than 2
    """
    if word1 == word2:
        return 0
    if len(word1) == len(word2):
        letter_count = 0
        for position, letter in enumerate(word1):
            if letter != word2[position]:
                letter_count += 1
        return letter_count

    if len(word1) > len(word2):
        if word1[1:] == word2:
            return 1
        elif word1[:-1] == word2:
            return 1
        else:
            return 1000

    if len(word2) > len(word1):
        if word2[1:] == word1:
            return 1
        elif word2[:-1] == word1:
            return 1
        else:
            return 1000

def sentence_difference(sentence1, sentence2):
    """
    Determine how different are two sentences in the same language
    :param word1: first sentence to compare
    :param word2: second sentence to compare
    :return: number of different characters or 1000 if more than 2
    """
    #TODO: improve sentence comparison algorithm
    return word_difference(sentence1, sentence2)
