# NumPy Indexing Roadmap

Tài liệu lộ trình học chi tiết dựa trên [`04-indexing.py`](file:///D:/machine-learning/01-numpy/01-fundamentals/04-indexing.py), giúp bạn đi từng bước từ cơ bản đến nâng cao và thực hành trực tiếp trên NumPy array.

> **Cách học gợi ý:** Đọc từng mục, gõ lại ví dụ và làm bài tập nhỏ vào [`04-indexing.py`](file:///D:/machine-learning/01-numpy/01-fundamentals/04-indexing.py), chạy kiểm tra bằng:
>
> ```powershell
> .\01-numpy\.venv\Scripts\python.exe .\01-numpy\01-fundamentals\04-indexing.py
> ```

---

## Tổng quan lộ trình

- [ ] **1. Basic Indexing – 1D Array** — Truy cập phần tử bằng index
- [ ] **2. Negative Indexing** — Truy cập phần tử từ cuối mảng
- [ ] **3. 2D Array Indexing** — Truy cập hàng, cột và phần tử
- [ ] **4. 3D Array Indexing** — Truy cập dữ liệu nhiều chiều
- [ ] **5. Multi-dimensional Indexing** — Sử dụng nhiều index trong cùng một biểu thức
- [ ] **6. Indexing và Assignment** — Thay đổi giá trị phần tử
- [ ] **7. Indexing với Boolean và Fancy Indexing** — Truy cập dữ liệu bằng điều kiện hoặc danh sách index
- [ ] **8. Review Exercises** — Bài tập tổng hợp kiểm tra toàn bộ kiến thức

---

## 1. Basic Indexing – 1D Array

**Mục tiêu:** Hiểu cách đánh số vị trí (index) trong mảng 1 chiều và truy cập đúng phần tử.

### Kiến thức cốt lõi
- NumPy sử dụng **0-based indexing**: phần tử đầu tiên ở vị trí `0`, phần tử thứ `n` ở vị trí `n - 1`.
- Cú pháp: `arr[index]`.
- Nếu `index >= len(arr)` hoặc `index < -len(arr)`, NumPy sẽ báo lỗi `IndexError`.

### Ví dụ minh họa
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[0])  # 10 (phần tử đầu tiên)
print(arr[2])  # 30 (phần tử thứ 3)
print(arr[4])  # 50 (phần tử cuối)
```

### Thực hành nhanh
- [ ] Tạo mảng `scores = np.array([7.5, 8.0, 6.5, 9.0, 8.5])`.
- [ ] In ra phần tử đầu tiên, phần tử ở giữa (`index = 2`), và tính tổng phần tử đầu + phần tử thứ 4.

---

## 2. Negative Indexing

**Mục tiêu:** Truy cập nhanh các phần tử tính từ cuối mảng mà không cần biết trước độ dài mảng.

### Kiến thức cốt lõi
- Index âm đếm từ cuối lên đầu:
  - `-1`: phần tử cuối cùng
  - `-2`: phần tử kế cuối
  - `-n`: phần tử đầu tiên (với `n = len(arr)`)
- Công thức quy đổi: `arr[-k]` tương đương `arr[len(arr) - k]`.

### Ví dụ minh họa
```python
import numpy as np

arr = np.array([10, 20, 30, 40, 50])

print(arr[-1])  # 50
print(arr[-2])  # 40
print(arr[-5])  # 10
```

### Thực hành nhanh
- [ ] Lấy phần tử cuối cùng và phần tử kế cuối của mảng `scores` bằng negative indexing.
- [ ] Kiểm tra biểu thức `scores[-1] == scores[len(scores) - 1]`.

---

## 3. 2D Array Indexing

**Mục tiêu:** Hình dung mảng 2D như một bảng (hàng × cột) và truy cập được từng phần tử, từng hàng, từng cột.

### Kiến thức cốt lõi
- Mảng 2D có `shape = (rows, cols)` (axis 0 là hàng, axis 1 là cột).
- Truy cập 1 phần tử: `arr[row, col]`.
- Truy cập cả 1 hàng: `arr[row]` hoặc `arr[row, :]`.
- Truy cập cả 1 cột: `arr[:, col]` (dấu `:` nghĩa là lấy toàn bộ theo chiều đó).

### Ví dụ minh họa
```python
import numpy as np

matrix = np.array([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])

print(matrix[0, 0])   # 1 (hàng 0, cột 0)
print(matrix[1, 2])   # 6 (hàng 1, cột 2)
print(matrix[-1, -1]) # 9 (hàng cuối, cột cuối)

print(matrix[1])      # [4 5 6] (cả hàng 1)
print(matrix[:, 1])   # [2 5 8] (cả cột 1)
```

### Thực hành nhanh
- [ ] Tạo ma trận `3x4` tùy ý.
- [ ] Lấy phần tử ở hàng 2, cột 3 (index `1, 2`).
- [ ] Lấy toàn bộ hàng cuối cùng và toàn bộ cột đầu tiên.

---

## 4. 3D Array Indexing

**Mục tiêu:** Đọc hiểu cấu trúc mảng 3 chiều (`(block, row, col)`) và truy cập chính xác từng lớp dữ liệu.

### Kiến thức cốt lõi
- Mảng 3D có `shape = (depth, rows, cols)`:
  - `axis 0`: lớp / block (tập các ma trận 2D)
  - `axis 1`: hàng trong từng ma trận
  - `axis 2`: cột trong từng hàng
- Truy cập 1 phần tử: `arr[block, row, col]`.
- Truy cập 1 ma trận 2D: `arr[block]`.
- Truy cập 1 hàng trong 1 block: `arr[block, row]`.

### Ví dụ minh họa
```python
import numpy as np

cube = np.array([
    [[1, 2, 3], [4, 5, 6]],
    [[7, 8, 9], [10, 11, 12]]
])
# shape: (2, 2, 3) -> 2 block, mỗi block 2 hàng, 3 cột

print(cube[0])        # Block 0 (mảng 2D 2x3)
print(cube[1, 0])     # Hàng 0 của Block 1 -> [7 8 9]
print(cube[1, 0, 2])  # Phần tử ở Block 1, hàng 0, cột 2 -> 9
```

### Thực hành nhanh
- [ ] Tạo mảng `arr3d = np.arange(24).reshape(2, 3, 4)`.
- [ ] In `arr3d.shape` để xác nhận kích thước.
- [ ] Truy cập phần tử cuối cùng của block thứ 2 bằng cả index dương và index âm.

---

## 5. Multi-dimensional Indexing

**Mục tiêu:** Thành thạo cú pháp gộp nhiều index trong một cặp ngoặc vuông và hiểu sự khác biệt với việc chain ngoặc vuông.

### Kiến thức cốt lõi
- Trong NumPy, luôn ưu tiên viết `arr[i, j, k]` thay vì `arr[i][j][k]`:
  - `arr[i, j, k]` truy cập trực tiếp một lần (nhanh hơn, rõ ràng hơn, hỗ trợ tốt hơn cho slicing/fancy indexing).
  - `arr[i][j][k]` tạo ra các mảng trung gian qua từng bước rồi mới lấy phần tử.
- Có thể kết hợp tự do index dương và index âm trong cùng một biểu thức, ví dụ `arr[-1, 0, -2]`.

### Ví dụ minh họa
```python
import numpy as np

arr = np.arange(12).reshape(3, 4)

# Nên dùng:
print(arr[1, -1])    # 7

# Hoạt động nhưng không khuyến khích:
print(arr[1][-1])    # 7
```

### Thực hành nhanh
- [ ] Viết lại 3 biểu thức truy cập 2D/3D từ dạng `arr[a][b]` sang `arr[a, b]`.
- [ ] Thử kết hợp index dương và âm trong cùng 1 biểu thức trên mảng 3D.

---

## 6. Indexing và Assignment

**Mục tiêu:** Cập nhật giá trị trong mảng bằng indexing và tránh các bẫy về kiểu dữ liệu (`dtype`) cũng như `view` vs `copy`.

### Kiến thức cốt lõi
- Gán 1 phần tử: `arr[0] = 99` hoặc `matrix[1, 2] = 100`.
- Gán cả hàng / cột: `matrix[0] = 0` (gán toàn bộ hàng 0 bằng `0`) hoặc `matrix[:, 1] = [10, 20, 30]`.
- **Lưu ý quan trọng về `dtype`:** Mảng NumPy có kiểu dữ liệu cố định. Nếu mảng có `dtype=int64` mà bạn gán `arr[0] = 9.9`, giá trị sẽ bị **cắt phần thập phân** thành `9` (không tự động chuyển mảng sang `float`).
- **Lưu ý về View:** Slicing hoặc lấy 1 hàng/cột tạo ra **view** (dùng chung bộ nhớ với mảng gốc). Thay đổi trên view sẽ làm thay đổi mảng gốc.

### Ví dụ minh họa
```python
import numpy as np

arr = np.array([1, 2, 3, 4])
arr[1] = 20
arr[-1] = 4.9  # Bị ép về int -> 4
print(arr)     # [ 1 20  3  4]

matrix = np.zeros((3, 3), dtype=int)
matrix[1, :] = 5
matrix[:, 2] = [7, 8, 9]
print(matrix)
```

### Thực hành nhanh
- [ ] Tạo mảng `a = np.array([10, 20, 30, 40])`, đổi phần tử thứ 2 thành `99`.
- [ ] Tạo ma trận `3x3` toàn số `0`, gán đường chéo chính (`[0,0]`, `[1,1]`, `[2,2]`) thành `1`.
- [ ] Thử gán số thực `3.75` vào mảng số nguyên và quan sát kết quả.

---

## 7. Indexing với Boolean và Fancy Indexing

**Mục tiêu:** Lọc dữ liệu theo điều kiện logic và trích xuất các phần tử ở những vị trí rời rạc bất kỳ.

### Kiến thức cốt lõi

#### A. Boolean Indexing (Masking)
- Tạo mảng boolean (mask) từ điều kiện: `mask = arr > 20`.
- Truyền mask vào `arr[mask]` hoặc viết gọn `arr[arr > 20]`.
- Kết hợp nhiều điều kiện bằng toán tử bitwise:
  - `&` (AND), `|` (OR), `~` (NOT) — **bắt buộc bọc mỗi điều kiện trong `()`**, ví dụ `arr[(arr > 10) & (arr < 40)]`.
- Có thể kết hợp với assignment: `arr[arr < 0] = 0`.

#### B. Fancy Indexing
- Truyền một **list hoặc mảng các index** để lấy nhiều phần tử không liên tiếp: `arr[[0, 2, 4]]`.
- Trên mảng 2D:
  - `matrix[[0, 2]]`: lấy hàng 0 và hàng 2.
  - `matrix[[0, 1], [1, 2]]`: lấy các cặp tọa độ `(0, 1)` và `(1, 2)`.
- **Lưu ý:** Cả Boolean Indexing và Fancy Indexing đều trả về **bản sao (copy)** chứ không phải view.

> Sau khi nắm phần này, bạn có thể luyện sâu thêm tại thư mục [`02-indexing-and-slicing/`](file:///D:/machine-learning/01-numpy/02-indexing-and-slicing/03-boolean-indexing.py).

### Ví dụ minh họa
```python
import numpy as np

arr = np.array([5, 12, 18, 25, 30, 7])

# Boolean Indexing
print(arr[arr > 15])                   # [18 25 30]
print(arr[(arr >= 10) & (arr <= 25)])  # [12 18 25]

# Fancy Indexing
indices = [0, 3, -1]
print(arr[indices])                    # [ 5 25  7]

matrix = np.arange(9).reshape(3, 3)
print(matrix[[0, 2], [1, 2]])          # Lấy (0,1)=1 và (2,2)=8 -> [1 8]
```

### Thực hành nhanh
- [ ] Cho `temps = np.array([22, 35, 28, 19, 40, 31])`. Lọc ra các ngày có nhiệt độ `>= 30`.
- [ ] Thay thế tất cả giá trị `< 25` trong `temps` bằng `25`.
- [ ] Dùng fancy indexing lấy các phần tử ở vị trí `0, 2, 4` của `temps`.

---

## 8. Review Exercises

**Mục tiêu:** Tự kiểm tra toàn bộ 7 nội dung trên qua một bộ bài tập tổng hợp.

### Bài tập tổng hợp (làm trong `04-indexing.py`)

1. **1D & Negative Indexing:**
   - Tạo mảng `data = np.array([15, 22, 8, 41, 33, 19, 50])`.
   - Lấy phần tử đầu tiên, phần tử thứ 4, và 2 phần tử cuối (dùng negative index).
2. **2D Indexing & Assignment:**
   - Tạo ma trận `scores` kích thước `4x3` (4 học sinh, 3 môn học) từ `np.arange(1, 13).reshape(4, 3)`.
   - In điểm của học sinh thứ 3 (index 2) ở môn thứ 2 (index 1).
   - In toàn bộ điểm của học sinh cuối cùng và toàn bộ điểm môn đầu tiên.
   - Tăng điểm của học sinh đầu tiên ở môn cuối cùng lên `99`.
3. **3D Indexing:**
   - Tạo mảng `3D` kích thước `(2, 2, 3)` bằng `np.arange(12).reshape(2, 2, 3)`.
   - Lấy phần tử ở block `1`, hàng `1`, cột `0`.
4. **Boolean & Fancy Indexing:**
   - Từ mảng `data` ở câu 1, lọc ra các số **chẵn** và **lớn hơn 10**.
   - Dùng fancy indexing lấy ra các phần tử tại vị trí `[1, 3, 5]`.
   - Đổi tất cả các giá trị `< 20` trong `data` thành `0`.

### Checklist hoàn thành
- [ ] Phân biệt được 0-based index dương và negative index.
- [ ] Đọc và truy cập đúng thứ tự `(row, col)` trên 2D và `(block, row, col)` trên 3D.
- [ ] Luôn dùng `arr[i, j]` thay vì `arr[i][j]`.
- [ ] Hiểu bẫy `dtype` khi gán giá trị mới vào mảng.
- [ ] Viết thành thạo Boolean mask (có ngoặc `()` khi dùng `&`, `|`) và Fancy indexing.
