nums = [3,0,1]
def missingnum(nums):
    result = len(nums)

    for i in range(len(nums)):
        result ^= i ^ nums[i]
    return result
print(missingnum(nums))    