def delete_letter(string_x: str, string_y: str):
   length_x = len(string_x)
   length_y = len(string_y)
   
   data = [[0] * (length_y + 1) for _ in range(length_x + 1)]

   for index in range(1, length_x + 1):
      
      for jndx in range(1, length_y + 1):
         
         if string_x[index - 1] == string_y[jndx - 1]:
            data[index][jndx] = data[index - 1][jndx - 1] + 1
         else:
            data[index][jndx] = max(data[index - 1][jndx], data[index][jndx - 1])

   return data[length_x][length_y]

string1 = "abcdesvbnvjkaskch"
string2 = "acehgfbhvbfdhv"

var = delete_letter(string1, string2)
extra_string = len(string1) + len(string2) - 2 * var

print(extra_string)