class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        prefix=[]
        pre=1
        suffix=[]
        suf=1
        ans=[]
        for i in nums:
            prefix.append(pre)
            pre*=i
        for i in range(len(nums)-1,-1,-1):
            suffix.append(suf)
            suf*=nums[i]
        suffix=suffix[::-1]
        for i in range(0,len(nums)):
            total=prefix[i]*suffix[i]
            ans.append(total)
        return ans