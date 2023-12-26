# Example using sorted()
# original_list = [3, 1, 4, 1, 5, 9, 2, 6, 5, 3, 5]
original_list=['a','ab','ba','b','abc']
sorted_list = sorted(original_list)
print("Original List:", original_list)
print("Sorted List:", sorted_list)

original_list.sort()
print("Original List (sorted in-place):", original_list)