# Sets
# Implement a function that takes two sets of integers as input and returns 
# a new set containing the intersection of the two sets.

def find_intersection(set1, set2):
    # Your code here
    # return set1.intersection(set2)

    # Or:
    result = set()
    for a in set1:
        for b in set2:
            if a == b:
                result.add(a)
    return result
    


# Test the function
set1 = {1, 2, 3, 4, 5}
set2 = {4, 5, 6, 7, 8}
# print(find_intersection(set1, set2))  # Expected output: {4, 5}


# ----------------------------------------------------------------------------------------------------------


# Implement a function that takes two sets of integers as input and returns a new set containing 
# the unique elements from both sets.

def merge_sets(set1, set2):
    # Your code here
    return set1.union(set2)

    


# Test the function
print(merge_sets(set1, set2))  # Expected output: {1, 2, 3, 4, 5, 6, 7, 8}
