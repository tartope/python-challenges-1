# Given a list of numbers, return the maximum value.

def max_value(nums):
  # todo
  # return max(nums)

  #or
  result = nums[0]
  for num in nums:
    if num > result:
      result = num
  return result

  pass 



# Test cases
print(max_value([4, 7, 2, 8, 10, 9]))
print(max_value([-5, -2, -1, -11]))

