class Solution:
    def romanToInt(self, s: str) -> int:
        n=len(s)
        ans=0
        mp = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
}  
        for i in range(0,n-1):
            if mp[s[i]]<mp[s[i+1]]:
                ans-=mp[s[i]]
            else:
                ans+=mp[s[i]]
        ans+=mp[s[n-1]]
        return ans


        