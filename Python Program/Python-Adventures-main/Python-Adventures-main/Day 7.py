def count_characters(words, chars):
    char_count = {}
    for char in chars:
        char_count[char] = char_count.get(char, 0) + 1

    total_length = 0
    for word in words:
        word_count = {}
        for char in word:
            word_count[char] = word_count.get(char, 0) + 1

        valid_word = True
        for char, count in word_count.items():
            if char not in char_count or count > char_count[char]:
                valid_word = False
                break

        if valid_word:
            total_length += len(word)

    return total_length

# Example 1
words1 = ["cat", "bt", "hat", "tree"]
chars1 = "atach"
output1 = count_characters(words1, chars1)
print("Example 1 Output:", output1)

# Example 2
words2 = ["hello", "world", "leetcode"]
chars2 = "welldonehoneyr"
output2 = count_characters(words2, chars2)
print("Example 2 Output:", output2)
