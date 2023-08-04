inp = input("Enter input: ")

#If length of the input is greater than 1 then process continues
if len(inp) > 1:
   #Creating necessary variables, "temp" for checking substrings in a temporary string and "longest_substring" for keeping a list of longest substrings
   temp = inp[0]
   longest_substring = []

   #Scanning the input
   i = 0
   while True:

      if inp[i + 1] in temp or i == len(inp) - 2:

         if i == len(inp) - 2 and inp[i + 1] not in temp:
            temp += inp[i + 1]

         if len(longest_substring) == 0:
            longest_substring.append(temp)

         elif len(longest_substring[0]) < len(temp):
            longest_substring = [temp]
            
         elif len(longest_substring[0]) == len(temp) and temp not in longest_substring:
            longest_substring.append(temp)

         i = i - (len(temp) - temp.index(inp[i + 1]) - 1)
         temp = inp[i + 1]
         i += 1

      else:
         temp += inp[i + 1]
         i += 1

      if i == len(inp) - 1:
         break
   
   #Printing the results
   for x in longest_substring:
      print(x + ", length: ", len(x))

else:
   if len(inp) == 0:
      print("You didn't enter any input!")
   else:
      print("Length of your input must be greater than 1!")