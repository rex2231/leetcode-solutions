class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        count = 1
        no_swap = False
        for i in range(len(nums)):
            if no_swap:
                break
            for j in range(i + 1, len(nums)):
                if nums[i] < nums[j]:
                    nums[i + 1], nums[j] = nums[j], nums[i + 1] 
                    count += 1
                    no_swap = False
                    break
                else:
                    no_swap = True
        return count
