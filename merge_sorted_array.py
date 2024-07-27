class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
            k=nums1[:m]
            j=nums2[:n]
            for i in j:
                k.append(i)
            k=sorted(k)
            for i in range(len(k)):
                nums1[i]=k[i]
        