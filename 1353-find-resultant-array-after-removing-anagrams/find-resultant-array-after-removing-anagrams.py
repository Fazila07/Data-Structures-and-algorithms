class Solution:
    def removeAnagrams(self, words: List[str]) -> List[str]:
        result=[]
        ans=[words[0]]
        for i in words[1:]:
            if sorted(i)!=sorted(ans[-1]):
                ans.append(i)
        return ans
        