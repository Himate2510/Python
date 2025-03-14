import array as arr
array_hi = arr.array('i', [1, 2, 3, 4, 5])
print("The original array is: ", array_hi)

print("Number of occurences of the number 3 in the array is: ", array_hi.count(3))
array_hi.reverse()
print("The reversed array is: ", array_hi)