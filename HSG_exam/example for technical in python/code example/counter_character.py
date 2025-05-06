def counter(string: str) -> int:
    
    strings = [str for str in string if str.isupper() == True]
 
  
 
    return len(strings)

print(counter("Ki thi chon HSG lop 9 Nam 2014"))