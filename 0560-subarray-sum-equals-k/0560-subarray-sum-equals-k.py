class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        dic={0:1}
        prefix=0
        count=0
        for x in nums:
            prefix+=x
            if prefix-k in dic:
                count+=dic[prefix-k]
            dic[prefix]=dic.get(prefix,0)+1
        return count