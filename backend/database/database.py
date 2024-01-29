from sqlalchemy import create_engine
from sqlalchemy.orm import declarative_base
from sqlalchemy.orm import sessionmaker

from utils.vars import variables

SQLALCHEMY_DATABASE_URL = f'mysql+pymysql://{variables["USERNAME"]}:{variables["PASSWORD"]}@{variables["HOSTDBNAME"]}:{variables["PORT"]}/{variables["DBNAME"]}'

engine = create_engine(
    SQLALCHEMY_DATABASE_URL
)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()