from database import db
from fastapi import FastAPI
from pydantic import BaseModel
from typing import Optional
from datetime import datetime

my_app = FastAPI()

db_con = db()
my_cursor = db_con.mydb.cursor()

# Học viên
class hoc_vien(BaseModel):
    id: Optional[int] = None
    name: str
    born: str
    address: Optional[str] = None
    email: Optional[str] = None

# Danh sách học viên
@my_app.get('/hocvien')
def index():
    my_cursor.execute("SELECT * FROM hocvien")
    hoc_vien = my_cursor.fetchall()

    if not hoc_vien:
        hoc_vien = "Danh sách học viên trống.\n"
    my_cursor.close()

    return hoc_vien

# Thêm học viên
@my_app.post('/hocvien/add')
def save(item: hoc_vien):
    birth_obj = datetime.strptime(item.born, '%d/%m/%Y')
    birth = datetime.strftime(birth_obj, '%Y-%m-%d')

    sql = "INSERT INTO hocvien (name, born, address, email) VALUES (%s, %s, %s)"
    val = (item.name, birth, item.address, item.email)
    my_cursor.execute(sql, val)
    print(db_con.mydb.commit())

    if my_cursor.rowcount > 0:
        message = f'Thêm mới học viên {birth} thành công!'
    else:
        message = f'Không thêm được học viên {item.name}'

    return message

# Chi tiết học viên
@my_app.get('/hocvien/{id}')
def detail(id: int):
    sql = "SELECT * FROM hocvien WHERE id = " + str(id)
    my_cursor.execute(sql)
    hoc_vien = my_cursor.fetchone()

    return hoc_vien

# Cập nhật học viên
@my_app.put('/hocvien/{id}')
def update(id: int, item: hoc_vien):
    return {"id": id, "item": item}

