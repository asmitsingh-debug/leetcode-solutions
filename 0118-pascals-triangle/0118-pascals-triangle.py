class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        n=numRows
        ans=[[1] for i in range(n)]
        for i in range(1,n):
            for j in range(1,i+1):
                if j==i:
                    ans[i].append(1)
                    break
                else:
                    s=ans[i-1][j-1]+ans[i-1][j]
                    ans[i].append(s)
        return ans