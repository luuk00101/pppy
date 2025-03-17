def custom_sort(word, order):
    # Create a list of indices from the order for each character in the word
    indices = [order.index(char) for char in word if char in order]

    # Sort the word based on these indices
    sorted_word = "".join([word[i] for i in sorted(indices)])

    return sorted_word
