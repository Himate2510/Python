def ways(stairs):
    if stairs < 0:
        return 0
    if stairs == 0:
        return 1
    two_steps = 0
    one_steps = 0

    if(stairs>=2):
        two_steps = ways(stairs-2)
    one_steps = ways(stairs-1)
    return one_steps + two_steps
stairs = int(input("Enter the number of stairs: "))

print("Number of ways to climb the stairs is: ", ways(stairs))