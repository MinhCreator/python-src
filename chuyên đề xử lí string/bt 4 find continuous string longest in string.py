# This function takes a string as input and finds the longest substring without repeating characters.
def find_longest_substring1(str1: str) -> str:
    # Initialize variables
    start = 0  # Start index of the current substring
    max_length = 0  # Length of the longest substring found so far
    longest_substring = ""  # The longest substring found so far
    character_count = {}  # Dictionary to store the last index of each character

    # Iterate over the string
    for end in range(len(str1)):
        # If the current character is already present in the substring and its last occurrence is after the start index,
        # update the start index to the next index of the repeating character
        if str1[end] in character_count and character_count[str1[end]] >= start:
            start = character_count[str1[end]] + 1

        # Update the last index of the current character
        character_count[str1[end]] = end
        print(character_count)

        # Update the max_length and longest_substring if a longer substring is found
        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substring = str1[start:end + 1]

    # Return the longest substring without repeating characters
    return longest_substring    
    


# import unittest
# class TestFindLongestSubstring(unittest.TestCase):
#     def test_find_longest_substring(self):
#         self.assertEqual(find_longest_substring1("abcabcbb"), "abc")
#         self.assertEqual(find_longest_substring1("bbbbb"), "b")
#         self.assertEqual(find_longest_substring1("pwwkew"), "wke")
#         self.assertEqual(find_longest_substring1(""), "")
#         self.assertEqual(find_longest_substring1("dvdf"), "vdf")

# if __name__ == '__main__':
#     unittest.main()


data_string = input("enter a string: ")
print(find_longest_substring1(data_string))