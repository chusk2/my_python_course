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


@app.route('/select')
def index():
    # List all .db files in DB_PATH as database names (without extension)
    databases = [p.stem for p in DB_PATH.iterdir() if p.suffix == ".db"]

    # On first load, no database is selected yet — request.args is empty
    # After the user selects a database and submits the form,
    # the value arrives as a query parameter: /select_db?database=inventario
    selected_db = request.args.get("database")

    tables = []
    columns = []
    selected_table = request.args.get("table")

    if selected_db:
        # Open the selected database and retrieve its table names
        db_file = DB_PATH / f"{selected_db}.db"
        conn, cursor = init_connection(str(db_file))
        tables = list_tables(cursor)

        if selected_table:
            # Fetch column names for the selected table using PRAGMA
            # PRAGMA table_info returns one row per column; index 1 is the column name
            rows = conn.execute(f"PRAGMA table_info({selected_table})").fetchall()
            columns = [row[1] for row in rows]

        conn.close()

    # Pass all values to the template:
    # - databases: populates the DB dropdown
    # - tables: populates the table dropdown (empty on first load)
    # - columns: populates the column checkboxes (empty until a table is selected)
    # - selected_db / selected_table: used to preserve selections across steps
    return render_template('select.html', databases=databases, tables=tables,
                           columns=columns, selected_db=selected_db, selected_table=selected_table)


@app.route("/read/<database>")
def read(database):
    # Table and selected columns come as query parameters:
    # /read/inventario?table=productos&columns=id&columns=nombre
    table = request.args.get("table")
    selected_columns = request.args.getlist("columns")  # returns a list of checked column names

    db_file = f"{Path('../sqlite_crud/data/') / database}.db"
    conn, cursor = init_connection(db_file)

    # PRAGMA table_info returns one row per column; index 1 is the column name
    all_columns = conn.execute(f'PRAGMA table_info({table})').fetchall()
    all_columns = [row[1] for row in all_columns]

    # Use selected columns if provided, otherwise show all
    columns = selected_columns if selected_columns else all_columns
    rows = read_table(table, cursor, cols=columns)

    return render_template("read.html", db = database, table = table,columns=columns, rows=rows)


if __name__ == "__main__":
    app.run(debug=True)
