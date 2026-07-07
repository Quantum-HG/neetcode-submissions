class Solution:
    def hasDuplicate(self, nums) -> bool:
        tracker = []
        for item in nums:
            if item not in tracker:
                tracker.append(item)
            else:
                # tracker[item] += 1
                return True
        return False