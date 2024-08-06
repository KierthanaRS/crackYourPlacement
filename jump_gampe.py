class Solution:
    def canJump(self, nums) -> bool:
        if 0 not in nums:
            return True
        if len(nums)==1:
            return True
        if nums[0]==0:
            return False
        
        z=[]
        n=len(nums)
        for i in range(len(nums)):
            if nums[i]==0:
                if i==n-1:
                    return True
                j=i-1
                while j>0 and i-j>=nums[j]:
                    j-=1
                if j==0 and i>=nums[0]:
                    return False
            else:
                if n-1-nums[i]<=0:
                    return True
        return True 
        