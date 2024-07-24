class Solution:
    def findDuplicate(self, nums):
        slow,fast=0,0
        while True:
            slow=nums[slow]
            fast=nums[nums[fast]]
            if slow==fast:
                break
        newslow=0
        while newslow != slow:
            newslow=nums[newslow]
            slow=nums[slow]
        return slow
sol = Solution()
nums=list(map(int,input().split()))
print(sol.findDuplicate(nums))