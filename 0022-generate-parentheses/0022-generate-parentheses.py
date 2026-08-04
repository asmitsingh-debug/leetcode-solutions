class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def solve(indx,bracket,res,total):
            
            if indx>=len(bracket):
                if total==0:
                    res.append("".join(bracket))
                return 
            if total>len(bracket)//2:
                return 
            elif total<0:
                return 
            bracket[indx]="("
            solve(indx+1,bracket,res,total+1)
            bracket[indx]=")"
            solve(indx+1,bracket,res,total-1)
        bracket=[""]*(n*2)
        res=[]
        solve(0,bracket,res,0)
        return res
        