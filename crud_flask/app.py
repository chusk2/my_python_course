from flask import Flask
from pathlib import Path
from crud import *


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"

@ app.route("/read/<database>/<table>")
def read(database, table):
    db_file = f"{Path("../sqlite_crud/data/") / database}.db"
    conn, cursor = init_connection(db_file)
    # read columns
    columns = conn.execute(f'PRAGMA table_info({table})')
    columns = [row[1] for row in cursor.fetchall()]
    
    return read_table("productos", cursor)

if __name__ == "__main__":
    app.run(debug=True)
