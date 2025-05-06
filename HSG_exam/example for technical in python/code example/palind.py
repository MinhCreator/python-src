def palind(string: str) -> str:

   if string == string[::-1]:
      return string

   else:
      list = []

      for i in string:
         list.append(i)

      index = 0
      len = 0
      string_new = ""
      print(list)
      while index < len(list):

         string_new = string_new + str(list[index::len])

         if string_new == string_new[::-1]:
            return string_new
         else:
            len += 1
            string_new = ""

         index = index + 1

      return string_new
