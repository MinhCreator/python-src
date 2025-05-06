'''bài của tôi'''
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

        # Update the max_length and longest_substring if a longer substring is found
        if end - start + 1 > max_length:
            max_length = end - start + 1
            longest_substring = str1[start:end + 1]

    # Return the longest substring without repeating characters
    return longest_substring , max_length, start

'''bài của cô'''
def substring_longest(string) -> str:
    
    max_len = 0
    len_present = 1

    for index in range(len(string)):
        checks = [string[index]]
        
        for index_2 in range(index + 1, len(string)):
            
            if string[index_2] not in checks:
                len_present += 1
                checks.append(string[index_2])
            else:
                break
        
        if len_present > max_len:
            max_len = len_present
            pos = index

        len_present = 1
        checks.clear()

    return string[pos:pos + max_len] # return string[pos:pos + max_len] là trả về 1 string 
    # return pos + 1, max_len thì trả về vị trí start của string và độ dài của string





# data_string = input("enter a string: ")
# print(substring_longest(data_string))





