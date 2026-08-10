class Solution:
    def search(self, nums: List[int], target: int) -> int:
        def is_blue(i):
            end = nums[-1]
            if nums[i] > end:
                return target <= nums[i] and target > end
            else:
                return target <= nums[i] or target > end
        
        l = -1
        r = len(nums)
        while l + 1 < r:
            mid = (l + r) // 2
            if is_blue(mid):
                r = mid
            else:
                l = mid
        return r if nums[r] == target else -1