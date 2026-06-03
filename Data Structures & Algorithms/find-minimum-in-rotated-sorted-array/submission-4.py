class Solution:
    def binSearch(self, arr, low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2

        if arr[(mid + 1) % len(arr)] < arr[mid]:
            return arr[(mid + 1) % len(arr)]

        right = self.binSearch(arr, mid + 1, high)
        left = self.binSearch(arr, low, mid - 1)

        return left if left != -1 else right

    def findMin(self, nums: List[int]) -> int:
        r = self.binSearch(nums, 0, len(nums) - 1)
        return r if r != -1 else nums[0]
        