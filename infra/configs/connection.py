from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
import os


class DBConnectionHandler:
    def __init__(self) -> None:
        self.__connection_string = os.getenv('DB_CONNECTION_STRING', 'mysql+pymysql://root:password@localhost:3306/db')
        self.__engine = self.__create_database_engine()

    def __create_database_engine(self):
        engine = create_engine(self.__connection_string)
        return engine
    
    def get_engine(self):
        return self.__engine
    
    def __enter__(self):
        session_maker = sessionmaker(bind=self.__engine)
        self.session = session_maker()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.session.close()
