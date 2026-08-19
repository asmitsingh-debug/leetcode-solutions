class Solution:
    def nextPermutation(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=n-2
        for i in range(n-1,0,-1):
            if nums[i]<=nums[i-1]:
                k-=1
            else:
                break
        if k==-1:
            nums[:]=nums[::-1]
        else:   
            for i in range(n-1,0,-1):
                if nums[i]>nums[k]:
                    nums[i],nums[k]=nums[k],nums[i]
                    break
            nums[k+1:]=nums[k+1:][::-1]
        