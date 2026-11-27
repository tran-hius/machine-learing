import numpy as np


arr = np.array([10, 20, 30], dtype=np.float32)

# ta có 8 bits = 1 byte
# float32 là 32 bits => float32 = 4 bytes
# float64 là 64 bits => float32 = 8 bytes
# vậy tại sao không dùng float32 cho tất cả?
# trong thực tế float32 thường hữu ích khi xử lý dữ liệu lớn, đặc biệt là trong deep learning
# float64 hữu ích khi cần độ chính xác số học cao hơn

print(arr)
print(arr.dtype)


arr1 = np.array([10, 20, 30], dtype=np.float32)
arr2 = np.array([10, 20, 30], dtype=np.float64)

# hiển thị ra số byte của từng phần tử chiếm
print(arr1.itemsize)
print(arr2.itemsize)

# tổng số byte của mảng
print(arr1.nbytes)
print(arr2.nbytes)


arrfl = np.array([1.9, 2.5, 3.8])
new_arr = arrfl.astype(np.int32)
print(arrfl)
print(new_arr)
