class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i=0
        v=set()
        while i<len(nums):
            if nums[i] in v:
                nums.pop(i)
            else:
                v.add(nums[i])
                i+=1
        return len(nums)
        