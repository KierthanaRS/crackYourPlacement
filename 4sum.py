class Solution:
    def fourSum(self, nums, target):
        ans=[]
        nums.sort()
        for a in range(len(nums)):
            if a>0 and nums[a] ==nums[a-1]:
                continue
            for b in range(a+1,len(nums)):
                if b>a+1 and nums[b]==nums[b-1]:
                    continue
                c,d=b+1,len(nums)-1
                while c<d:
                    s=nums[a]+nums[b]+nums[c]+nums[d]
                    if s==target:
                        ans.append([nums[a],nums[b],nums[c],nums[d]])
                        while c<len(nums)-1 and nums[c]==nums[c+1]:
                            c+=1
                        while d>0 and nums[d]==nums[d-1]:
                            d-=1
                        d-=1
                        c+=1
                    elif s<target:
                        c+=1
                    else:
                        d-=1
        return ans
                


        