class Solution:
    def quicksort_3way(self, nums, left, right):
        if left >= right:
            return
        pivot = nums[left]
        # lt: 小于 pivot 的区域右边界
        # gt: 大于 pivot 的区域左边界
        # i: 当前遍历的位置
        lt, i, gt = left, left + 1, right
        while i <= gt:
            if nums[i] < pivot:
                nums[lt], nums[i] = nums[i], nums[lt]
                lt += 1
                i += 1
            elif nums[i] > pivot:
                nums[i], nums[gt] = nums[gt], nums[i]
                gt -= 1
            else:
                i += 1
        # 递归排序小于和大于的区域
        self.quicksort_3way(nums, left, lt - 1)
        self.quicksort_3way(nums, gt + 1, right)

    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        if n != 0:
            i = m
            j = 0
            while i < m + n and j < n:
                nums1[i] = nums2[j]
                i += 1
                j +=1
        
        self.quicksort_3way(nums1,0,m+n-1)
        return nums1