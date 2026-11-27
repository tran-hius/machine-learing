import numpy as np

arr = np.array([15, 25, 35, 45, 55, 65, 75])
# Truy cập phần tử đầu tiên
# print(arr[0])  # 10


# Truy cập phần tử cuối cùng
# print(arr[4])
# print(arr[-1])


data = np.array(
    [
        [12, 45, 67, 23, 89],
        [34, 78, 21, 56, 90],
        [11, 65, 88, 42, 31],
        [99, 24, 53, 76, 18],
        [43, 87, 29, 61, 72],
        [55, 13, 94, 38, 47],
    ]
)

# 2. Level 1 – Slicing nâng cao

# Bài 1. Lấy 3 học sinh đầu tiên và 3 môn học đầu tiên.
b1 = data[:3, :3]
print(b1)
# Giải thích bài 1 ta có :3 tức là lấy tất cả trục y học sinh trước index số 2 và lấy tất cả trục x trước index số 2

# Bài 2. Lấy toàn bộ học sinh nhưng chỉ lấy các môn ở vị trí 1, 3.
b2 = data[:, 1:4:2]
print("b2", b2)

# Bài 3. Lấy 3 học sinh cuối cùng, đảo ngược thứ tự các môn học.
b3 = data[3:]
print("b3", b3[:,::-1])

# Bài 4. Lấy các học sinh ở vị trí 0, 2, 4 và các môn ở vị trí 0, 2, 4.
b4 = data[:6:2, :5:2]
print("b4", b4)

# Bài 5. Lấy toàn bộ dữ liệu nhưng đảo ngược cả hàng lẫn cột.
b5 = data[::-1, ::-1]
print("b5", b5)

# Bài 6. Lấy vùng dữ liệu hình chữ nhật gồm:
# Học sinh từ index 1 đến 4.
# Môn học từ index 2 đến 4.
b6 = data[1:5, 2:5]
print("b6", b6)


# 3. Level 2 – Boolean Indexing

# Bài 7. Lấy tất cả điểm lớn hơn hoặc bằng 70.
b7 = data[data >= 70]
print("b7", b7)