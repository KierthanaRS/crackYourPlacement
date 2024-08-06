from itertools import permutation
class Solution:
    def uniquePerms(self, arr, n):
        return list(sorted(set(permutations(arr))))
                