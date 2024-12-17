from threading import Lock

import pandas as pd
import redis
from sqlalchemy import MetaData, create_engine
from sqlalchemy.sql import expression


class __DatabaseConnection:
    def __init__(
        self, database="mysql+pymysql://root:change_me@localhost:3306/portfolio"
    ):
        self.database = database
        self.__engine = create_engine(self.database, echo=False)
        self._MetaData = MetaData

    def _create_session(self, query):
        with self.__engine.connect() as conn:
            response = conn.execute(query)
            conn.commit()
            return response


class Querying(__DatabaseConnection):
    async def Send(self, sql) -> pd.DataFrame | None:
        if isinstance(sql, expression.Insert):
            response = self._create_session(sql)
            return response
        response = self._create_session(sql)
        df = pd.DataFrame(self._create_session(sql))
        return df

class Cache:
    _instance = None
    _lock = Lock()

    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            with cls._lock:
                if not cls._instance:
                    cls._instance = super(Cache, cls).__new__(cls)
                    cls._instance.connection =  cls.make_connection()
        return cls._instance
    
    def get_connection(self):
        return self.connection

    def make_connection():
        return  redis.Redis(host="localhost", port=6379, decode_responses=True)
    
    
    