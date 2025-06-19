number_largest = int(input("Enter the largest number for which you want to find the GCD of :  "))
number_smallest = int(input("Enter the smallest number for which you want to find the GCF of:  "))

while(number_smallest):
    numberStore = number_smallest
    number_smallest = number_largest % number_smallest
    number_largest = numberStore

print("The GCD of the 2 numbers given is: ", number_largest)