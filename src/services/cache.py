import json
from pymemcache.client import base
from pymemcache.exceptions import MemcacheIllegalInputError


class CacheService():
    def __init__(self):
        self.cache = base.Client(('localhost', 11211))

    def set_command(self, client_id, command):
        key = bytes([client_id])
        val = bytes(json.dumps(command), encoding='utf8')
        self.cache.set(key, val)  


    def get_command(self, client_id):
        data = {}
        key = bytes([client_id])

        result = self.cache.get(key)
        if result:
            data = json.loads(result.decode('utf-8'))

        return data

    def __repr__(self):
        return f'<CacheService()>'