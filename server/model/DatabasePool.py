import os
from dotenv import load_dotenv
from mysql.connector import connect, Error

load_dotenv()

class DatabasePool:
    @staticmethod
    def getConnection():
        try:
            host = os.getenv('DB_HOST')
            database = os.getenv('DB_DATABASE')
            user = os.getenv('DB_USER')
            password = os.getenv('DB_PASSWORD')

            connection = connect(
                host=host,
                database=database,
                user=user,
                password=password
            )

            return connection

        except Error as e:
            print(e)