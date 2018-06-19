
class Solution:
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        if len(S)==0:
            return ""
        ret_S = list(S)
        ind_dict = {}
        for i,value in enumerate(indexes):
            ind_dict[value] = [sources[i],targets[i]]
        indexes.sort(reverse=True)
        
        for i,index in enumerate(indexes):
            if index<len(S)and S[index:].startswith(ind_dict[index][0]):
                ret_S[index:index+len(ind_dict[index][0])] = ind_dict[index][1]
            else:
                continue
        return "".join(ret_S)
            
sol =Solution()
print(sol.findReplaceString("vmokgggqzp",[3,5,1],["kg","ggq","mo"],["s","so","bfr"]))



