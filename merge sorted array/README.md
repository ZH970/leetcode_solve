## 主要思想就是合并和排序两步，要不就把两个数组合并后排序，要不就用双指针法直接合并排序。

### 方法一：合并后排序
没难度，主要记住一两个快速的排序方法
这里用了快排：
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
