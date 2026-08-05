class Solution:
    def combinationSum3(self, k: int, n: int) -> List[List[int]]:
        def sumk(indx, subset, target,total=0):
            if total == target and len(subset)==k:
                result.append(subset.copy())
                return
            if indx==len(candidates):
                return 
            if len(subset)>k:
                return
            if total+candidates[indx]>target:
                return 

            # include
            if total + candidates[indx] <= target:
                subset.append(candidates[indx])
                sumk(indx+1, subset, target,total + candidates[indx])
                subset.pop()

            # exclude
            sumk(indx+1, subset, target,total)
        result=[]
        subset=[]
        candidates=[i for i in range(1,10)]
        sumk(0,subset,n)
        return result