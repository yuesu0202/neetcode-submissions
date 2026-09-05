class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        def is_blue(i):
            end = nums[-1]
            if nums[i] >= end:
                return target > end and target <= nums[i]
            else:
                return target > end or target <= nums[i]
        

        l = -1
        r = len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if is_blue(mid):
                r = mid
            else:
                l = mid
        return True if nums[r] == target else False