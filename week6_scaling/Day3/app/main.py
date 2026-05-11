from fastapi import FastAPI
from contextlib import asynccontextmanager
import redis.asyncio as redis
import json


# Redis + App Lifecycle
@asynccontextmanager
async def lifespan(app: FastAPI):
    app.state.redis = redis.Redis(
        host="localhost",
        port=6379,
        decode_responses=True
    )
    print("Redis connected")

    yield

    await app.state.redis.close()
    print("Redis disconnected")


app = FastAPI(lifespan=lifespan)


# Root Endpoint
@app.get("/")
async def root():
    return {"message": "FastAPI + Redis is running 🚀"}


# Set value in Redis
@app.post("/set/{key}")
async def set_value(key: str, value: str):
    await app.state.redis.set(key, value)
    return {"status": "stored", "key": key, "value": value}


# Get value from Redis
@app.get("/get/{key}")
async def get_value(key: str):
    value = await app.state.redis.get(key)

    if value is None:
        return {"error": "Key not found"}

    return {"key": key, "value": value}


# Cached API example
@app.get("/user/{user_id}")
async def get_user(user_id: int):
    redis_key = f"user:{user_id}"

    cached = await app.state.redis.get(redis_key)

    if cached:
        return {
            "source": "redis",
            "data": json.loads(cached)
        }

    # Simulated DB response
    user_data = {
        "id": user_id,
        "name": f"User-{user_id}",
        "role": "ML Engineer"
    }

    # Store in Redis with expiration
    await app.state.redis.set(
        redis_key,
        json.dumps(user_data),
        ex=60  # cache for 60 seconds
    )

    return {
        "source": "database",
        "data": user_data
    }