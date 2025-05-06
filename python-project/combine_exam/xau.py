def find_longest_str(string: str):
   dicts = {}
   max_len = 0
   for index in range(len(string)):

      for jndex in range(index + 1,len(string)):
         sub_string = string[index : jndex]
         dicts[sub_string] = dicts.get(sub_string, 0) + 1

         for sub, count in dicts.items(): 
            if len(sub) > max_len and count >= 2: max_len = len(sub)

   return max_len

def find_longest_str1(string: str):
    max_len = 0
    for index in range(len(string)):
        seen = set()
        for jndex in range(index + 1, len(string)):
            if string[jndex] in seen:
                max_len = max(max_len, jndex - index)
                break
            seen.add(string[jndex])
    return max_len - 2 if max_len > 0 else 0 


    
st = 'trutrutiktiktappop'
sa = 'sabcabcfabc'
ad = 'abcdef'
print(find_longest_str1(ad))