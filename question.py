#Taking input from the user
val = input("Enter value: ")

#If length of the value is greater than 1 then process continues
if len(val) > 1:
   #Creating necessary variables, "temp" for checking substrings in a temporary string and "longest_substring" for keeping a list of longest substrings
   temp = ""
   longest_substring = []

   #Scanning the value
   for i in range(len(val) - 1):
      #We need to scan the value starting from every letter to the end of the value to not miss any substrings, to do that, we need nested two loops
      temp = val[i]
      #Scanning the rest of the value starting from the current letter
      for j in range(i, len(val) - 1):
         #If we came to an end for the current substring because our temporary substring contains the next letter of the value on the scan
         if val[j + 1] in temp:
            #If the list doesn't contain any substrings we add temporary substring into it
            if len(longest_substring) == 0:
               longest_substring.append(temp)
            #If the length of the substring we keep in the list is smaller than the length of the temporary substring, the list now only contains the temporary substring
            elif len(longest_substring[0]) < len(temp):
               longest_substring = [temp]
            #If the length of the substring we keep in the list is equal to the length of the temporary substring and we aren't keeping the same substring already, we add the temporary substring to the list
            elif len(longest_substring[0]) == len(temp) and temp not in longest_substring:
               longest_substring.append(temp)
            #After checking and editing of the list is done, temporary substring is set to the next letter of the value on the scan by breaking the inner loop
            break
            #PS: We only check if we came to an end for a better time complexity
         #If temporary substring doesn't contain the next letter of the value on the scan, we add it to the temporary substring
         else:
            temp += val[j + 1]
         #We need to check again before exiting the inner loop to not miss a substring
         if j == len(val) - 2:
            if len(longest_substring) == 0:
               longest_substring.append(temp)
            elif len(longest_substring[0]) < len(temp):
               longest_substring = [temp]
            elif len(longest_substring[0]) == len(temp) and temp not in longest_substring:
               longest_substring.append(temp)
   
   #Printing the results
   for x in longest_substring:
      print(x + ", length: ", len(x))

#If length of the value is not greater than 1 then process comes to an end
else:
   if len(val) == 0:
      print("You didn't enter any value!")
   else:
      print("Length of your value must be greater than 1!")

#Time Complexity (worst case) : O((N-1)^2 + c)
#Space Complexity : O(N + c)