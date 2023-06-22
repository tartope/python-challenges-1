# Given a string, return the most frequent character within that string.

def most_frequent_char(s):
  # todo
  # Store occurences of each letter in dict
  char_count = {}
  # Loop through string
  for char in s:
    # If char is in dict
    if char in char_count:
      # Increment its value
      char_count[char] += 1
    else:
      # else, if char is not in dict then add it and give it a value of 1
      char_count[char] = 1
  # Compare the # of occurences
  max_count = 0
  letter = ''
  for k, v in char_count.items():
    if max_count < v:
      max_count = v
      letter = k
  # return the letter wiht highest number
  return letter
  pass 




# Test cases
print(most_frequent_char('bookeeper')) # -> 'e'
print(most_frequent_char('david')) # -> 'd'