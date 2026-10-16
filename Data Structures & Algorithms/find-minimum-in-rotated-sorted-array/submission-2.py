class Solution:
    def findMin(self, nums: List[int]) -> int:
        start = 0
        end = len(nums)-1

        while start < end:
            mid = (start + end) // 2

            if nums[mid] > nums[end]:
                start = mid + 1   # drop is to the right of mid, so mid can't be the min
            else:
                end = mid       # mid..hi is sorted, so min is at mid or to its left

        return nums[start]   