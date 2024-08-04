from collections import defaultdict
class Solution:
    def subarraysDivByK(self, nums, k: int):
        dp=[0]*(len(nums)+1)
        d=defaultdict(int)
        for i in range(1,len(nums)+1):
            dp[i]=dp[i-1]+nums[i-1]
            d[dp[i]%k]+=1
        ans=0
        for i in d.keys():
            if i==0:
                ans+=d[i]
          
            ans+=(d[i]*(d[i]-1)//2)

        return ans
        