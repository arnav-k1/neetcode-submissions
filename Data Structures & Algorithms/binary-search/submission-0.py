class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        
        end = (len(nums) - 1)
        start = 0

        while start <= end:
            mid_val = nums[(start+end)//2]

            if mid_val == target:
                return ((start+end)//2)

            if target < mid_val:
                end = ((start+end)//2) - 1

            if target > mid_val:
                start = ((start+end)//2) + 1

        return (-1)