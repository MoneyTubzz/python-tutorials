arr = [64, 34, 25, 12, 22, 11, 90]
print("Unsorted array is:", arr)

if len(arr) > 1:
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]

if len(left_half) > 1:
    mid_left = len(left_half) // 2
    left_left_half = left_half[:mid_left]
    left_right_half = left_half[mid_left:]

if len(right_half) > 1:
    mid_right = len(right_half) // 2
    right_left_half = right_half[:mid_right]
    right_right_half = right_half[mid_right:]


left_left_half.sort()
left_right_half.sort()
right_left_half.sort()
right_right_half.sort()

arr = left_left_half + left_right_half + right_left_half + right_right_half
    
print("Sorted array is:", arr)