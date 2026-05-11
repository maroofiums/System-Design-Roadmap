from fastapi import FastAPI, Depends
from sqlalchemy import create_engine, Column, Integer, String, Index
from sqlalchemy.orm import sessionmaker, declarative_base, Session


# DATABASE CONFIG (POOLING)
DATABASE_URL = "postgresql://postgres:password@localhost:5432/mydb"

engine = create_engine(
    DATABASE_URL,
    pool_size=10,          # connection pooling
    max_overflow=20,
    pool_timeout=30,
    pool_pre_ping=True
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()


# MODEL (INDEXING INCLUDED)
class User(Base):
    __tablename__ = "users"

    id = Column(Integer, primary_key=True, index=True)
    name = Column(String(100))
    email = Column(String(100), unique=True, index=True)  # indexed column

# Explicit index (good practice for optimization tracking)
Index("idx_email", User.email)


# Create tables (for learning purpose)
Base.metadata.create_all(bind=engine)


# FASTAPI APP
app = FastAPI()


# DB DEPENDENCY
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# OPTIMIZED QUERY (NO SELECT *)
@app.get("/users/{user_id}")
def get_user(user_id: int, db: Session = Depends(get_db)):
    # Only selecting required columns (optimization)
    user = (
        db.query(User.id, User.name, User.email)
        .filter(User.id == user_id)
        .first()
    )

    if not user:
        return {"error": "User not found"}

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


# INDEXED SEARCH QUERY
@app.get("/users/search/")
def search_user(email: str, db: Session = Depends(get_db)):
    # This uses indexed column (email)
    user = (
        db.query(User.id, User.name, User.email)
        .filter(User.email == email)
        .first()
    )

    if not user:
        return {"error": "User not found"}

    return {
        "id": user.id,
        "name": user.name,
        "email": user.email
    }


# BULK FETCH (LIMITED = OPTIMIZED)
@app.get("/users/")
def list_users(limit: int = 10, db: Session = Depends(get_db)):
    users = (
        db.query(User.id, User.name, User.email)
        .limit(limit)
        .all()
    )

    return [
        {"id": u.id, "name": u.name, "email": u.email}
        for u in users
    ]