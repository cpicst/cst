from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base

# DATABASE_URL = "mysql+pymysql://root:@localhost:3306/training"
DATABASE_URL = "postgresql+psycopg2://cpi_qzt5_user:7GfApwZeO5b8WUSc8mx15eDZb5AdsQgZ@dpg-dc36gm0m7kps73dbdf9g-a.ohio-postgres.render.com/cpi_qzt5"

engine = create_engine(DATABASE_URL)
session_local = sessionmaker(autocommit = False, autoflush= False, bind=engine)
base = declarative_base()
