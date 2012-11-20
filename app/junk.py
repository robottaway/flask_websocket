import redis

pool = redis.ConnectionPool()

rclient = redis.Redis(connection_pool=pool)

