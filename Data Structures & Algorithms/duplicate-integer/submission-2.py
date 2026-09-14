class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        seen_so_far = set()
        for i in range(len(nums)):
            current = nums[i]
            if current in seen_so_far:
                return True
            seen_so_far.add(current)
        return False