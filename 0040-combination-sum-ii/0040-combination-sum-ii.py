class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def sumk(indx, subset, target,total=0):
            if total == target:
                result.append(subset.copy())
                return

            if indx == len(candidates):
                return
            if total+candidates[indx]>target:
                return 

            for i in range(indx,len(candidates)):
                if i>indx and candidates[i]==candidates[i-1]:
                    continue
                subset.append(candidates[i])
                sumk(i+1,subset, target,total+candidates[i])
                subset.pop()
        result=[]
        subset=[]
        sumk(0,subset,target)
        return result