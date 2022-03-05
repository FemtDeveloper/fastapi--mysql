from sqlalchemy import create_engine, MetaData

engine = create_engine('mysql+pymysql://root:532526@localhost:3306/storedb')

conn = engine.connect()

meta = MetaData()