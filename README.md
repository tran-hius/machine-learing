# Machine Learning

Kho lưu trữ tài liệu và bài tập thực hành lộ trình học **Machine Learning** bằng Python — từ xử lý mảng số học, thao tác dữ liệu bảng, trực quan hóa đến xây dựng và đánh giá mô hình học máy.

## Lộ trình & Cấu trúc thư mục

| STT | Course | Thư viện chính | Nội dung chính |
| --- | --- | --- | --- |
| 01 | [`01-numpy/`](./01-numpy/) | `numpy` | Fundamentals, Indexing & Slicing, Array Operations, Shape Manipulation, Aggregation, Broadcasting, Linear Algebra |
| 02 | [`02-pandas/`](./02-pandas/) | `pandas` | Series, DataFrame, Data Cleaning, Data Filtering |
| 03 | [`03-matplotlib/`](./03-matplotlib/) | `matplotlib` | Basic Plots, Customization |
| 04 | [`04-scikit-learn/`](./04-scikit-learn/) | `scikit-learn` | Preprocessing, Supervised Learning, Unsupervised Learning, Model Evaluation |

```text
machine-learning/
├── 01-numpy/
│   ├── 01-fundamentals/
│   ├── 02-indexing-and-slicing/
│   ├── 03-array-operations/
│   ├── 04-shape-manipulation/
│   ├── 05-aggregation/
│   ├── 05-broadcasting/
│   ├── 06-linear-algebra/
│   └── README.md
├── 02-pandas/
│   ├── 01-series/
│   ├── 02-dataframe/
│   ├── 03-data-cleaning/
│   ├── 04-data-filtering/
│   └── README.md
├── 03-matplotlib/
│   ├── 01-basic-plots/
│   ├── 02-customization/
│   └── README.md
├── 04-scikit-learn/
│   ├── 01-preprocessing/
│   ├── 02-supervised-learning/
│   ├── 03-unsupervised-learning/
│   ├── 04-model-evaluation/
│   └── README.md
├── .gitignore
└── README.md
```

## Môi trường thực hành

Mỗi course được tách riêng một môi trường ảo Python (`.venv`, Python 3.12) để quản lý thư viện độc lập.

### Kích hoạt môi trường (Windows PowerShell)

Ví dụ với course `01-numpy`:

```powershell
Set-ExecutionPolicy -Scope Process -ExecutionPolicy RemoteSigned
.\01-numpy\.venv\Scripts\Activate.ps1
```

Hoặc chạy trực tiếp một file bài tập mà không cần kích hoạt shell:

```powershell
.\01-numpy\.venv\Scripts\python.exe .\01-numpy\01-fundamentals\01-create-array.py
```

### Cài đặt lại môi trường (nếu clone repo về máy mới)

Sử dụng [`uv`](https://docs.astral.sh/uv/) để tạo lại `.venv` và cài thư viện cho từng course:

```powershell
# 01-numpy
uv venv --python 3.12 01-numpy\.venv
uv pip install --python 01-numpy\.venv\Scripts\python.exe numpy

# 02-pandas
uv venv --python 3.12 02-pandas\.venv
uv pip install --python 02-pandas\.venv\Scripts\python.exe pandas

# 03-matplotlib
uv venv --python 3.12 03-matplotlib\.venv
uv pip install --python 03-matplotlib\.venv\Scripts\python.exe matplotlib

# 04-scikit-learn
uv venv --python 3.12 04-scikit-learn\.venv
uv pip install --python 04-scikit-learn\.venv\Scripts\python.exe scikit-learn
```
