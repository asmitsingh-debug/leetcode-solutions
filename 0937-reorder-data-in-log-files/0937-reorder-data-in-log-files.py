class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        dic={'letter':[],'digi':[]}
        for char in logs:
            if char[-1].isdigit():
                dic['digi'].append(char)
            else:
                dic['letter'].append(char)
        dic['letter'].sort(key=lambda x: (x.split(' ', 1)[1], x.split(' ', 1)[0]))
        ans=[]
        ans.extend(dic['letter'])
        ans.extend(dic['digi'])
        return ans 