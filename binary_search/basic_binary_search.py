def binary_search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            start = mid + 1
        else:
            end = mid - 1
    return -1

if __name__ == "__main__":
    arr = [1, 3, 5, 7, 9, 11]
    print(binary_search(arr, 7))   # Output: 3
    print(binary_search(arr, 4))   # Output: -1
