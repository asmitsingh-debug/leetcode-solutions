class Solution:
    def uniformArray(self, nums1: list[int]) -> bool:
        od = float('inf')

        for x in nums1:
            if x % 2 != 0:
                od = min(od, x)
        if od!=float('inf'):
            for x in nums1:
                if x % 2 == 0 and x < od:
                    return False
        
        return True