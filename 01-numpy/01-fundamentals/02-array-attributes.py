import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr)
print(arr.size) #Tổng số phần tử của mảng
print(arr.ndim) #Số chiều của mảng
print(arr.shape) #Kích thước từng chiều
print(arr.dtype) #Kiểu dữ liệu của phần tử

arr1 = np.zeros((3, 2, 4))
print(arr1.tolist())
print(arr1.ndim)
print(arr1.shape)
