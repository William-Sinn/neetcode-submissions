class Solution:
    def binSearch(self, arr, low, high):
        if low > high:
            return -1
        
        mid = (low + high) // 2
        print(arr[mid])

        if arr[(mid + 1) % len(arr)] < arr[mid]:
            return arr[(mid + 1) % len(arr)]

        if arr[low] > arr[mid]:
           return self.binSearch(arr, low, mid)

        if arr[high] < arr[mid]:
            return self.binSearch(arr, mid + 1, high)

        return -1

    def findMin(self, nums: List[int]) -> int:
        r = self.binSearch(nums, 0, len(nums) - 1)
        return r if r != -1 else nums[0]
        