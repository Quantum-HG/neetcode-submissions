class Solution:
    def hasDuplicate(self, nums) -> bool:
        tracker = set()
        for item in nums:
            if item not in tracker:
                tracker.add(item)
            else:
                return True
        return False
# Searching in dictionary is way faster than using lists