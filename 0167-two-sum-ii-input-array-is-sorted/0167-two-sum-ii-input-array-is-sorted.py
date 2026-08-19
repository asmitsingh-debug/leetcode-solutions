class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        dic={}
        for i in range(0,len(numbers)):
            tar=target-numbers[i]
            if tar in dic:
                return [dic[tar]+1,i+1]
            else:
                dic[numbers[i]]=i