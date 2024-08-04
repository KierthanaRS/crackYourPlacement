class Solution:
    def findDuplicates(self, nums):
        ans=[]
        for i in range(len(nums)):
            a=abs(nums[i])
            if nums[a-1]<0:
                ans.append(a)
            else:
                nums[a-1]*=-1
        return ans

        