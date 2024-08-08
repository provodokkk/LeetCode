# Time Complexity: O(log(n))

class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        def findFirst() -> int:
            left, right = 0, len(nums) - 1
            index = -1

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    right = mid - 1
                elif nums[mid] > target:
                    right = mid - 1
                else:
                    left = mid + 1
            return index
        
        def findLast(start: int) -> int:
            if start == -1:
                return -1

            left, right = start, len(nums) - 1
            index = start

            while left <= right:
                mid = (left + right) // 2
                if nums[mid] == target:
                    index = mid
                    left = mid + 1
                elif nums[mid] < target:
                    left = mid + 1
                else:
                    right = mid - 1

            return index

        start = findFirst()
        end = findLast(start)
        
        return [start, end]
