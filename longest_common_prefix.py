class Solution:
    def longestCommonPrefix(self, strs) -> str:
        res=strs[0]
        if len(strs)==1:
            return strs[0]
        for i in range(1,len(strs)):
            r=""
            for j in range(min(len(res),len(strs[i]))):
                if res[j]==strs[i][j]:
                    r+=strs[i][j]
                else:
                    break
            res=r
            if res=="":
                break
        return res
        