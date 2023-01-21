# Write a program to create a tuple and a list. Convert the list to tuple and display the
# elements of both. Write the program to remove the duplicate element of the list.

def removeDuplicates(lst):
	
	return [t for t in (set(tuple(i) for i in lst))]
		
# Driver code
lst = [(1, 2), (5, 7), (3, 6), (1, 2)]
print(removeDuplicates(lst))
