# FastAPI Auto Career

## Mô tả dự án
Đây là một API đơn giản để quản lý thông tin người dùng sử dụng FastAPI và SQLite.

## Cấu trúc dự án
project_name/
├── app/
│   ├── __init__.py
│   ├── main.py                 # Điểm vào chính của ứng dụng (entry point)
│   ├── core/                   # Cấu hình cốt lõi và các tiện ích
│   │   ├── __init__.py
│   │   ├── config.py           # Cấu hình ứng dụng (ví dụ: biến môi trường)
│   ├── db/                     # Cấu hình cơ sở dữ liệu
│   │   ├── __init__.py
│   │   ├── base.py             # Định nghĩa base cho các model
│   │   ├── crud.py             # Các thao tác CRUD (Create, Read, Update, Delete)
│   │   ├── database.py         # Kết nối cơ sở dữ liệu và session
│   ├── models/                 # Định nghĩa các bảng cơ sở dữ liệu bằng SQLAlchemy
│   │   ├── __init__.py
│   │   ├── user.py             # Bảng users trong cơ sở dữ liệu
│   ├── api/                    # Các endpoint API
│   │   ├── __init__.py
│   │   ├── v1/                 # Phiên bản 1 của API
│   │   │   ├── __init__.py
│   │   │   ├── endpoints/      # Các module chứa các API endpoint
│   │   │   │   ├── __init__.py
│   │   │   │   ├── users.py    # Ví dụ API endpoint: /users
│   ├── schemas/                # Định nghĩa các Pydantic models (schema)
│   │   ├── __init__.py
│   │   ├── user.py             # Schema cho User
│   ├── tests/                  # Thư mục chứa các bài kiểm thử cho ứng dụng
│   │   ├── __init__.py
│   │   ├── test_main.py        # Các bài test cho API chính
├── alembic/                    # Thư mục cho Alembic migration
│   ├── versions/               # Chứa các file migration cho cơ sở dữ liệu
│   ├── env.py                  # File cấu hình của Alembic
│   ├── script.py.mako          # Mẫu script migration
├── .env                        # File chứa biến môi trường (ví dụ: DATABASE_URL)
├── .gitignore                  # Các file và thư mục cần bỏ qua khi commit vào git
├── requirements.txt            # Danh sách các thư viện cần thiết
├── README.md                   # Tài liệu mô tả dự án
