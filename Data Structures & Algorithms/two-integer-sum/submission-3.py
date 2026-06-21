class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        arr = sorted(nums)
        L = 0
        R = len(arr) - 1
        while L < R:
            current = arr[L] + arr[R]
            if current > target:
                R -= 1
            if current < target:
                L += 1
            if current == target:
                if arr[L] == arr[R]:
                    first = nums.index(arr[L])
                    second = nums.index(arr[R], first + 1)
                    return sorted([first, second])
                else:
                    return sorted([nums.index(arr[L]), nums.index(arr[R])])
        
            

