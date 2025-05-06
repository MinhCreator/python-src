# hàm hoán vị strings
def hoan_vis(hoan_vi: str, string2: str) -> str:
    """
    Perform a transformation on string2 based on the given hoan_vi pattern.

    Args:
        hoan_vi (str): The pattern used to rearrange the characters in string2.
        string2 (str): The string to be transformed.

    Returns:
        str: The transformed string.
    """
    # Calculate the number of characters in string2
    char = len(string2)

    # Calculate the number of times hoan_vi should be repeated to cover string2
    sl_group = char // len(hoan_vi) + 1

    # Extend string2 with whitespace to make its length a multiple of hoan_vi's length
    string2 += " " * (sl_group * len(hoan_vi) - char)
    
    # Split string2 into groups of characters with the same length as hoan_vi
    list_group = [string2[i:i + len(hoan_vi)] for i in range(0, char, len(hoan_vi))]
    print(list_group)

    # Encode each group of characters based on the hoan_vi pattern
    encode_list_group = []

    for group in range(len(list_group)):

        # Rearrange the characters in the group according to the hoan_vi pattern
        encode = "".join([list_group[group][int(var) - 1] for var in hoan_vi])
        
        print(encode)
        
        encode_list_group.append(encode)

    # Join the encoded groups together to form the final transformed string
    return "".join(encode_list_group)
    
n = 4
hoan_vi = "3241"                
string2 = "english"

print(hoan_vis(hoan_vi, string2))
