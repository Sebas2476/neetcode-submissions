class Solution:
    def findMin(self, nums: List[int]) -> int:
        low = 0
        high = len(nums) - 1

        while low < high:
            mid = (low + high) // 2

            if nums[mid] > nums[high]:
                low = mid + 1   # drop is to the right of mid, so mid can't be the min
            else:
                high = mid       # mid..hi is sorted, so min is at mid or to its left

        return nums[low]   