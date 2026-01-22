class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        i=0
        j=len(nums)-1
        while (i<=j):
            if nums[j] == val:
                j-=1
            elif nums[i] != val:
                i+=1
            elif nums [i] == val:
                nums[i] = nums[j]
                j-=1
                i+=1
        print(nums)
        print(i,j)
        return i


