from sqlalchemy import create_engine, MetaData
import pymysql
from dotenv import load_dotenv
import os
from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String
import sqlalchemy

load_dotenv()

user = os.getenv("USER_DB")
password = os.getenv("PASSWORD_DB")
host = os.getenv("HOST_DB")
port = os.getenv("PORT_DB")
name_db = os.getenv("NAME_DB")

engine = create_engine(f'mysql+pymysql://root@{host}:{port}/{name_db}', pool_recycle=3600)

meta = MetaData()
if not sqlalchemy.inspect(engine).has_table("cpu"):
    metadata = MetaData(engine)
    Table('cpu', metadata,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('price', Integer),
    )
    metadata.create_all()
conn = engine.connect()