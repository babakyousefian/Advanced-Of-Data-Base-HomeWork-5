from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base


# SQLALCHEMY_DATABASE_POSTGRESQL_URL = "postgresql://postgres:1234@localhost:5432/LorestanUniv.db"

SQLALCHEMY_DATABASE_POSTGRESQL_URL = "sqlite:///./lorestanUniv.db"

engine = create_engine(SQLALCHEMY_DATABASE_POSTGRESQL_URL)

sessionLocal = sessionmaker(autocommit=False , autoflush=False , bind=engine)

Base = declarative_base()