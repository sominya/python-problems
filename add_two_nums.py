# Given a list of numbers and a target number.
# Find the index of the first 2 numbers which sum up to the target
# Example nums = [2,7,11,15], target =9 , answer is [0,1]
def find_sums(nums, target):
    out=[]
    for i in nums:
        if target-i in nums:
            out.append(nums.index(i))
            out.append(nums.index(target-i))
            return out
