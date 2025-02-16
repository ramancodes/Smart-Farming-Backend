from psycopg2 import Error

def create_table(connection):
    try:
        cursor = connection.cursor()
        cursor.execute("""
            CREATE TABLE IF NOT EXISTS users (
                userid VARCHAR(255) PRIMARY KEY,
                email VARCHAR(255) UNIQUE NOT NULL,
                password VARCHAR(255) NOT NULL,
                name VARCHAR(255) NOT NULL,
                gender VARCHAR(10),
                contact INT,
                location VARCHAR(255),
                dob DATE,
                registrated_on TIMESTAMP NOT NULL
            )
        """)
        connection.commit()
        return True
    except Error as e:
        print(f"Table Not Created. The error '{e}' occurred")
        return False