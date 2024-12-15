import pandas as pd
from sqlalchemy import MetaData, create_engine
from sqlalchemy.sql import expression

class __DatabaseConnection:
    def __init__(
        self, database="mysql+pymysql://root:qwerty@localhost:3306/portfolio"
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
