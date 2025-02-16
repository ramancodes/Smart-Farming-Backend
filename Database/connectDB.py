import psycopg2
from psycopg2 import Error

class DB:
    def __init__(self, host, database, user, password):
        self.host = host
        self.database = database
        self.user = user
        self.password = password
        self.connection = None

    def connect(self):
        try:
            self.connection = psycopg2.connect(
                host=self.host,
                database=self.database,
                user=self.user,
                password=self.password
            )
            print("PostgreSQL Database connected")
        except Error as e:
            print(f"Database Not Connected. The error '{e}' occurred")
        return self.connection

    