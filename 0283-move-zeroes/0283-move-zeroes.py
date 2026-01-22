class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
    #    i = 0
    #    j = len(nums)-1

    #    while (i<=j):
    #     if nums[j] == 0:
    #         j-=1
    #     elif nums[i] != 0:
    #         i+=1
    #     elif nums[i] == 0 and nums[j] != 0:
    #         nums[i],nums[j] = nums[j], nums[i]
    #         i+=1

        zero = 0
        for i in range(len(nums)):
            if nums[i] == 0:
                zero+=1
        while 0 in nums:
            nums.remove(0)
        for i in range(zero): nums.append(0)