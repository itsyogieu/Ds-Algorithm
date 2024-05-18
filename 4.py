def reverse_array(arr, start, end):
    while start < end:
        arr[start], arr[end] = arr[end], arr[start]
        start += 1
        end -= 1

def rotate_array(nums, k):
    n = len(nums)
    k = k % n
    reverse_array(nums, 0, n - 1)
    reverse_array(nums, 0, k - 1)
    reverse_array(nums, k, n - 1)
input_array = [3, 8, 9, 2, 5]
k = 2
rotate_array(input_array, k)
print("Rotated Array:", input_array)
