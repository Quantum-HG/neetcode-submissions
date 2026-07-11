class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic = {}
        for index, num in enumerate(nums):
            dic[num] = index
        
        for index, num in enumerate(nums):
            other_num = (target - num)
            if other_num in dic: 
                other_num_index = dic[(target - num)]
                if other_num_index != index: # the number should be different and not self
                    return [index, dic[(target - num)]]