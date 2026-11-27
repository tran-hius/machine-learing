import numpy as np

# ==========================================
# 1. Thuộc tính cơ bản của mảng 1D
# ==========================================
arr_1d = np.array([10, 20, 30, 40, 50])

print("Mảng 1D:", arr_1d)
print("ndim (số chiều):", arr_1d.ndim)
print("shape (kích thước từng chiều):", arr_1d.shape)
print("size (tổng số phần tử):", arr_1d.size)
print("dtype (kiểu dữ liệu):", arr_1d.dtype)

# ==========================================
# 2. Thuộc tính của mảng nhiều chiều (3D)
# ==========================================
arr_3d = np.zeros((3, 2, 4))  # 3 block, mỗi block 2 hàng x 4 cột

print("\nMảng 3D:\n", arr_3d)
print("ndim (số chiều):", arr_3d.ndim)
print("shape (kích thước từng chiều):", arr_3d.shape)
print("size (tổng số phần tử):", arr_3d.size)
print("dtype (kiểu dữ liệu):", arr_3d.dtype)
