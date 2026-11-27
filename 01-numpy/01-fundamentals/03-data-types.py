import numpy as np

# ==========================================
# 1. Chỉ định kiểu dữ liệu khi tạo mảng
# ==========================================
# 8 bits = 1 byte
# - float32: 32 bits = 4 bytes -> tiết kiệm RAM/VRAM, thường dùng trong Deep Learning
# - float64: 64 bits = 8 bytes -> mặc định của NumPy, dùng khi cần độ chính xác cao
arr_f32 = np.array([10, 20, 30], dtype=np.float32)
print("arr_f32:", arr_f32, "| dtype:", arr_f32.dtype)

# ==========================================
# 2. So sánh bộ nhớ: itemsize & nbytes
# ==========================================
arr_f64 = np.array([10, 20, 30], dtype=np.float64)

# itemsize: số byte mỗi phần tử chiếm
# nbytes: tổng số byte toàn mảng chiếm (size * itemsize)
print(f"float32 -> itemsize: {arr_f32.itemsize} bytes, nbytes: {arr_f32.nbytes} bytes")
print(f"float64 -> itemsize: {arr_f64.itemsize} bytes, nbytes: {arr_f64.nbytes} bytes")

# ==========================================
# 3. Ép kiểu dữ liệu với .astype()
# ==========================================
arr_float = np.array([1.9, 2.5, 3.8])
arr_int = arr_float.astype(np.int32)  # Cắt bỏ phần thập phân (không làm tròn)

print("\nTrước khi ép kiểu:", arr_float, "| dtype:", arr_float.dtype)
print("Sau khi ép kiểu:  ", arr_int, "| dtype:", arr_int.dtype)
