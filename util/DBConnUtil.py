import mysql.connector
from exception.DatabaseConnectionException import DatabaseConnectionException

def get_connection(db_config):
    try:
        connection = mysql.connector.connect(
            host=db_config["host"],
            port=db_config["port"],
            database=db_config["database"],
            user=db_config["user"],
            password=db_config["password"]
        )
        return connection
    except Exception as e:
        raise DatabaseConnectionException(str(e))
