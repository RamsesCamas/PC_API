from sqlalchemy import Table, Column
from sqlalchemy.sql.sqltypes import Integer, String, Date, Text

from config.db import meta


cpu = Table('cpu', meta,
    Column('id', Integer, primary_key=True),
    Column('name', String(255)),
    Column('price', Integer),
    )