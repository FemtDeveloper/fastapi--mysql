from sqlalchemy import Integer, String, Table, Column
from config.db import meta, engine
import sys
sys.path.append('..')


users = Table('users', meta, Column(
    'id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('email', String(255), unique=True),
    Column('password', String(255)))

meta.create_all(engine)
