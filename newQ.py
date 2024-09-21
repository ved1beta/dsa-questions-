# Bubble sort

L = [5,1,2,3,6]

# Get the length of the list
n = len(L)

# Outer loop to keep track of passes
for i in range(1,n): # values i = 1, ... , n-1
# Alternatively the below for loop also works
# (Make sure you use the corresponding 2nd j loop too)
# for i in range(n-1) # values i = 0, ..., n-2

# Variable to count the number of comparisons
  count = 0
# Inner loop to perform pairwise comparisons
  for j in range(n-i): #values j = 0, 1, ..., n-i-1
# Alternatively the below for loop also works
# for j in range(n-i-1) #values j = 0, 1, ..., n-i-2
    # Compare the pairs of elements
    if L[j] > L[j+1]:
      # Swap
      L[j] , L[j+1] = L[j+1], L[j]
    count += 1
# Print the number of comparisons per pass
  print("Pass:",i)
  print("No. of comparisons:",count)

print("After Bubble sort:")
print(L)
# Selection sort

L = [2, 5, 3, 1, 4]

# Get the length of the list
n = len(L)

# Outer loop to indicate number of passes
for i in range(n-1): # i = 0, 1, ..., n-2
# pos - variable to hold the current position, at which the smallest value to be inserted
# min - variable to hold the index of the smallest element
  pos = i
  min = i

# Inner loop to go through further indices and select the smallest value
  for j in range(i+1,n): # j = i+1, i+2, ..., n-1
# If any index j is founf such that it has a smaller element than min, update min
    if L[j] < L[min]:
      min = j
  #swap L[min] and L[pos]
  L[min] , L[pos] = L[pos], L[min]

print("Result of selection sort:")
print(L)
# Insertion sort

L = [2, 5, 3, 1, 4]

# Get the length of the list
n = len(L)

# Outer loop to run through all indices for inserting new elements
for i in range(1,n):
# key is the current element to be inserted
  key = L[i]
  j = i-1

# Compare the new element with all the lower indices and
# shift the old element at index j by 1 position to make room for new element
# repeat until: either j goes negative or new element is greater than element at j
  while j>=0 and key < L[j]:
    L[j+1] = L[j]
    j = j-1

# Insert the new element at it's suitable position - j+1
  L[j+1] = key

print("Result of insertion sort:")
print(L)
