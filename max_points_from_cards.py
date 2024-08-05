class Solution:
    def maxScore(self, cardPoints: List[int], k: int) -> int:
        if len(cardPoints)==k:
            return sum(cardPoints)
        
        ms=sum(cardPoints[:k])
        s=ms
        for i in range(1,k+1):
           s=s-cardPoints[k-i]+cardPoints[-i]
           ms=max(ms,s)
        return ms


        