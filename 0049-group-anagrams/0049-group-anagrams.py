class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        dict={}
        res=[]
        for char in strs:
            if "".join(sorted(char)) in dict:
                dict["".join(sorted(char))].append(char)
            else:
                dict["".join(sorted(char))]=[]
                dict["".join(sorted(char))].append(char)
        for keys,val in dict.items():
            val.sort()
            res.append(val)
        return res
        
            