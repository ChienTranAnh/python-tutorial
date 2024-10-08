from datetime import datetime
from passlib.context import CryptContext

def format_date(date: str):
    date_obj = datetime.strptime(date, '%d/%m/%Y')
    return date_obj.strftime('%Y-%m-%d')

def crypt_pass():
    return CryptContext(schemes=["bcrypt"], deprecated="auto")
