class Pair:

    def Hi(self, nums, target):

        look = {}

        for i, num in enumerate(nums):
            if target - num in look:
                return (look[target - num], i)
            look[num] = i
obj = Pair()
target = int(input("Enter the target number: "))
nums = [10, 20 ,30 ,40 ,50, 60, 70]
print( obj.Hi(nums, target))