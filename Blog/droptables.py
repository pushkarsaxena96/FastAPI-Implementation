from sqlalchemy import create_engine, MetaData, Table
from sqlalchemy.orm import sessionmaker

# create engine to connect to SQLite database
engine = create_engine('sqlite:///blog.db')

# create metadata object and reflect existing tables in database
metadata = MetaData()
metadata.reflect(bind=engine)

# create session factory and session
Session = sessionmaker(bind=engine)
session = Session()

# specify table(s) to delete
tables_to_delete = ['blogs', 'user','user_access']

# loop through tables to delete and drop them
for table_name in tables_to_delete:
    if table_name in metadata.tables:
        metadata.tables[table_name].drop(bind=engine)

# commit changes to database
engine.connect().commit()

print("Tables deleted successfully.")