from fastapi import APIRouter, Response, status
from config.db import conn
from models.user import users
from schemas.user import User
from cryptography.fernet import Fernet
from starlette.status import HTTP_200_OK


user = APIRouter()
key = Fernet.generate_key()

f = Fernet(key)


@user.get('/')
def welcome():
    return 'Welcome to my api'


@user.get('/users',  tags=['Users'])
def get_users():
    return conn.execute(users.select()).fetchall()


@user.get('/users/{id}', tags=['Users'])
def get_user_by_id(id: str):
    return conn.execute(users.select().where(users.c.id == id)).first()


@user.post('/users', response_model=User, tags=['Users'])
def create_user(user: User):
    new_user = {'name': user.name.capitalize(),
                'email': user.email}
    new_user['password'] = f.encrypt(user.password.encode('utf-8'))
    result = conn.execute(users.insert().values(new_user))
    print(result)
    return conn.execute(users.select().where(users.c.id == result.lastrowid)).first()


@user.delete('/users/{id}', status_code=status.HTTP_204_NO_CONTENT, tags=['Users'])
def delete_user_by_id(id: str):
    conn.execute(users.delete().where(users.c.id == id))
    return Response(status_code=HTTP_200_OK)


@user.put('/users/{id}', tags=['Users'])
def update_user(id: str, user: User):
    conn.execute(users.update().values(name=user.name, email=user.email,
                 password=f.encrypt(user.password.encode('utf-8'))).where(users.c.id == id))
    return 'user updated'
