from sqlalchemy import create_engine, MetaData

engine = create_engine(
    'mysql+pymysql://admin:a532526Z@da-test.c1trjg34drld.us-east-2.rds.amazonaws.com/test')
# 'mysql+pymysql://root:532526@localhost/storedb')

conn = engine.connect()

meta = MetaData()
