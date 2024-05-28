import os
import pg8000

def connect_to_db():
    try:
        conn = pg8000.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            host=os.getenv("DB_HOST"),
            port=int(os.getenv("DB_PORT", 5432)),  # Default to 5432 if not set
            database=os.getenv("DB_NAME")
        )
        print("Connection to database established successfully.")
        return conn
    except Exception as e:
        print(f"Error connecting to the database: {e}")
        return None

def disconnect_from_db(conn):
    if conn:
        try:
            conn.close()
            print("Disconnected from the database.")
        except Exception as e:
            print(f"Error disconnecting from the database: {e}")



def main(params):
  name = params.get("name", "world")
  greeting = "Hello " + name + "!"

  connection = connect_to_db()
  
  disconnect_from_db(connection)

  return {
        "headers": {
            "Content-Type": "application/json",
        },
        "statusCode": 200,
        "body": params,
  }
