from sqlalchemy import create_engine,Column,Integer,Float
from sqlalchemy.orm import sessionmaker, declarative_base

DATABASE_URL = "sqlite:///./test.db"

engine = create_engine(
    DATABASE_URL,
    echo=True
)

Base = declarative_base()

class Prediction(Base):
    __tablename__ = "predictions"

    id = Column(Integer,primary_key=True,index=True)
    value = Column(Float)

Base.metadata.create_all(bind = engine)

SessionLocal = sessionmaker(bind=engine)
session = SessionLocal()

def insert_data(value = 0.0):
    new_prediction = Prediction(value=value)
    session.add(new_prediction)
    session.commit()
    print("Data Inserted!...")

def read_data():
    data = session.query(Prediction).all()
    print("Stored Data: \n")
    for row in data:
        print(f"| ID: {row.id} | Value: {row.value} |")

if __name__ == "__main__":
    insert_data(49.9)
    read_data()