import zmq
import json
import sqlite3

context = zmq.Context()
socket = context.socket(zmq.REP)
socket.bind("tcp://*:5555")


while True:
    conn = sqlite3.connect("database.db")
    conn.row_factory = sqlite3.Row
    cursor = conn.cursor()
    #  Wait for next request from client
    message = socket.recv()
    if message.decode() == 'QUIT': # Client asked server to quit
        break
    elif "CREATE" in message.decode(): # Client asked for secret message
        print("create request")
        payload = message.decode().split("CREATE")[1] #Get JSON from here
        payload = json.loads(payload)
        try:
            # Database connection
            cursor.execute(
                """
                INSERT INTO posts (first_name, last_name, shifts, days_working, trained_rotations, comments)
                VALUES (?, ?, ?, ?, ?, ?)
                """,
                (
                    payload["first_name"],
                    payload["last_name"],
                    payload["shifts"],
                    payload["days_working"],
                    payload["trained_rotations"],
                    payload["comments"],
                ),
            )
            conn.commit()
            # Fetching data after insertion
            cursor.execute("SELECT * FROM posts")
            cursor.close()
            conn.close()
            print("finished request")
            socket.send(b"Successfully added shift to DB")
        except sqlite3.Error:
            socket.send(b"ERROR: SQL ERROR")
            
    elif "FETCH" in message.decode(): # Client asked for secret message
        print("fetch request")
        try:
            # Database connection
            cursor.execute("SELECT * FROM posts")
            rows = cursor.fetchall()  # Get all rows
            data = [list(row) for row in rows] # Turn into lists
            # If more than 8 employees, return scroll flag
            flag = "True" if len(data) >= 8 else "False";
            cursor.close()
            conn.close()
            
            jsonObj = {
                "data": data,
                "scroll": flag
            }
            
            jsonObj = json.dumps(jsonObj)
            socket.send_string(jsonObj)
        except sqlite3.Error as e:
            print(f"SQLite error: {e}")
            socket.send(b"ERROR: SQL ERROR")