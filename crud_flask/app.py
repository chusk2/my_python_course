# Flask CRUD Application
# This app provides a web interface to browse SQLite databases and their tables.
#
# Routes:
#   GET /             - Home page
#   GET /select_db    - Database and table selector
#   GET /read/<db>    - Display rows of a table from the selected database

from flask import Flask, render_template, request
from pathlib import Path
from crud import *

# Path to the folder containing all .db files
DB_PATH = Path("../sqlite_crud/data")

app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, Flask!"


@app.route('/select_db')
def index():
    # List all .db files in DB_PATH as database names (without extension)
    databases = [p.stem for p in DB_PATH.iterdir() if p.suffix == ".db"]

    # On first load, no database is selected yet — request.args is empty
    # After the user selects a database and submits the form,
    # the value arrives as a query parameter: /select_db?database=inventario
    selected_db = request.args.get("database")

    tables = []
    if selected_db:
        # Open the selected database and retrieve its table names
        db_file = DB_PATH / f"{selected_db}.db"
        conn, cursor = init_connection(str(db_file))
        tables = list_tables(cursor)
        conn.close()

    # Pass databases, tables, and selected_db to the template.
    # - databases: populates the first dropdown
    # - tables: populates the second dropdown (empty on first load)
    # - selected_db: used to build the action URL of the second form
    return render_template('select_db.html', databases=databases, tables=tables, selected_db=selected_db)


@app.route("/read/<database>")
def read(database):
    # The table name comes as a query parameter: /read/inventario?table=productos
    table = request.args.get("table")

    db_file = f"{Path('../sqlite_crud/data/') / database}.db"
    conn, cursor = init_connection(db_file)

    # PRAGMA table_info returns one row per column; index 1 is the column name
    columns = conn.execute(f'PRAGMA table_info({table})')
    columns = [row[1] for row in columns.fetchall()]

    rows = read_table(table, cursor)

    return render_template("read.html", db = database, table = table,columns=columns, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
