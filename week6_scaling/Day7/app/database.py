from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

DATABASE_URL = "postgresql://postgres:whynot@db:5432/ml_db"

engine = create_engine(DATABASE_URL)
SessionLocal = sessionmaker(bind=engine)