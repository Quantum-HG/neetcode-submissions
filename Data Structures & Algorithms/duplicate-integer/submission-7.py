class Solution:
    def hasDuplicate(self, nums) -> bool:
        tracker = {}
        for item in nums:
            if item not in tracker:
                tracker[item] = 1
            else:
                return True
        return False
# Searching in dictionary is way faster than using lists