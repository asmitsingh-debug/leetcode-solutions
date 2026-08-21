class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        while val  in nums:
            i=nums.index(val)
            nums.pop(i)
        return len(nums)