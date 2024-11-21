import redis

from core.settings import REDIS_CONFIG


_redis_client = redis.Redis(
    host=REDIS_CONFIG.get("REDIS_HOST", "localhost"),
    port=REDIS_CONFIG.get("REDIS_PORT", 6379),
    decode_responses=True,
)


def redis_set(key: str, value: str, exp_time: int):
    _redis_client.set(key, value, ex=exp_time)


def redis_get(key: str) -> str:
    return _redis_client.get(key)


def redis_delete(key: str):
    _redis_client.delete(key)
