class Solution:

    def findMinDiff(self, A,N,M):
        A.sort()
        min_diff=float('inf')
        for i in range(0,N-M+1):
            min_diff=min(min_diff,A[i+M-1]-A[i])
        return min_diff