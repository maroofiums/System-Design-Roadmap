import redis 
import json

r = redis.Redis(
    host="redis",
    port = 6379,
    decode_responses=True
)

def get_cache(key):
    data = r.get(key)
    if data:
        return json.loads(data)
    return None

def set_cache(key,value):
    r.setex(key,60,json.dumps(value))
    