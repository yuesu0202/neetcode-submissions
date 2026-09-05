class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        ## heap solution
        # min_heap = []
        # for i in range(len(nums)):
        #     if len(min_heap) < k:
        #         heapq.heappush(min_heap, nums[i])
        #     else:
        #         if min_heap[0] < nums[i]:
        #             heapq.heappop(min_heap)
        #             heapq.heappush(min_heap, nums[i])
        # return min_heap[0]


        k = len(nums) - k
        
        def quickSelect(l, r):
            pivot, p = nums[r], l
            for i in range(l, r):
                if nums[i] < pivot:
                    temp = nums[i]
                    nums[i] = nums[p]
                    nums[p] = temp
                    p += 1
            nums[p], nums[r] = nums[r], nums[p]

            if p == k:
                return nums[p]
            elif p < k:
                return quickSelect(p+1, r)
            else:
                return quickSelect(l, p-1)
        return quickSelect(0, len(nums)-1)
