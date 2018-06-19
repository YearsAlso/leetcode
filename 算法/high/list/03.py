class Solution:
    def fourSumCount(self, A, B, C, D):
        """
        :type A: List[int]
        :type B: List[int]
        :type C: List[int]
        :type D: List[int]
        :rtype: int
        """
        dict1 = {}
        dict2 = {}
        indexs = 0
        for i, a in enumerate(A):
            for j, b in enumerate(B):
                if dict1.get(a + b):
                    dict1[a + b] += 1
                else:
                    dict1[a + b] = 1
        
        for i, c in enumerate(C):
            for j, d in enumerate(D):
                if dict2.get(c + d):
                    dict2[c + d]+=1
                else:
                    dict2[c + d] = 1
        
        for key, value in dict1.items():
            have_key = dict2.get(0 - key)
            if have_key:
                indexs+=value*have_key
        
        return indexs


sol = Solution()
print(sol.fourSumCount([-1, -1],
                       [-1, 1],
                       [-1, 1],
                       [1, -1]))
