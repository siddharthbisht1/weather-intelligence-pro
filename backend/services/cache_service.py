import time

# Simple In-Memory Cache Store
_cache_store = {}
CACHE_EXPIRY = 3600  # 1 hour in seconds

def get_cached_data(key: str):
    if key in _cache_store:
        data, timestamp = _cache_store[key]
        if time.time() - timestamp < CACHE_EXPIRY:
            return data
        else:
            del _cache_store[key]  # Cache expired
    return None

def set_cached_data(key: str, data: dict):
    _cache_store[key] = (data, time.time())