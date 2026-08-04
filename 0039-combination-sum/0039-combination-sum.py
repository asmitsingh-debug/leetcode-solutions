class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        def sumk(indx, subset, target,total=0):
            if total == target:
                result.append(subset.copy())
                return

            if indx == len(candidates):
                return
            if total+candidates[indx]>target:
                return 

            # include
            if total + candidates[indx] <= target:
                subset.append(candidates[indx])
                sumk(indx, subset, target,total + candidates[indx])
                subset.pop()

            # exclude
            sumk(indx+1, subset, target,total)
        result=[]
        subset=[]
        sumk(0,subset,target)
        return result