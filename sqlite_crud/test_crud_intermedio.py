import sqlite3
import unittest

# ── Functions copied from CRUD_intermedio.ipynb ────────────────────────────────

def list_tables(conn, cursor):
    tables = (cursor
              .execute("SELECT name FROM sqlite_master WHERE type='table'")
              .fetchall())
    return [i[0] for i in tables if i[0] != "sqlite_sequence"]


def create_table(table_name, query, conn, cursor):
    if table_name not in list_tables(conn, cursor):
        cursor.execute(query)
        conn.commit()


def populate_table(table, cols, values, data_structure="dict", conn=None, cursor=None):
    if data_structure not in ["tuples", "dict"]:
        return None

    if data_structure != "dict":
        values = [{k: v for k, v in zip(cols, t)} for t in values]

    placeholders = ", ".join(f":{c}" for c in cols)
    query = f"insert into {table} ({', '.join(cols)}) values ({placeholders}) ;"
    cursor.executemany(query, values)
    conn.commit()


def read_table(table, cols="*", filter=None, limit=None, cursor=None):
    columns = ", ".join(cols) if cols != "*" else "*"
    query = f"select {columns} from {table}"
    if filter:
        query += f" where {filter}"
    if limit:
        query += f" limit {limit}"
    query += " ;"
    return cursor.execute(query).fetchall()


def truncate_table(table, conn=None, cursor=None):
    cursor.execute(f"delete from {table} ;")
    cursor.execute(f'delete from sqlite_sequence where name="{table}" ;')
    conn.commit()


def drop_table(table, cursor=None):
    cursor.execute(f"drop table {table} ;")


def delete_records(table, filter="", cursor=None):
    if not filter:
        return None
    cursor.execute(f"delete from {table} where {filter} ;")


def update_records(table, col, value, filter="", conn=None, cursor=None):
    query = f"update {table} set {col} = ?"
    if filter:
        query += f" where {filter}"
    query += " ;"
    cursor.execute(query, (value,))
    conn.commit()


# ── Test helpers ───────────────────────────────────────────────────────────────

CREATE_PRODUCTOS = """
    CREATE TABLE IF NOT EXISTS productos (
        id              INTEGER PRIMARY KEY AUTOINCREMENT,
        nombre          TEXT    NOT NULL,
        marca           TEXT    NOT NULL,
        categoria       TEXT    NOT NULL,
        precio          REAL    NOT NULL,
        stock           INTEGER NOT NULL,
        especificaciones TEXT,
        fecha_ingreso   TEXT
    )
"""

COLS = ["nombre", "marca", "categoria", "precio", "stock", "especificaciones", "fecha_ingreso"]

SAMPLE_PRODUCTS = [
    {"nombre": "iPhone 15 Pro", "marca": "Apple", "categoria": "Smartphones",
     "precio": 999.99, "stock": 10, "especificaciones": "6.1 pulgadas", "fecha_ingreso": "2024-01-01"},
    {"nombre": "Galaxy S24", "marca": "Samsung", "categoria": "Smartphones",
     "precio": 899.99, "stock": 5, "especificaciones": "6.2 pulgadas", "fecha_ingreso": "2024-01-02"},
    {"nombre": "MacBook Pro", "marca": "Apple", "categoria": "Laptops",
     "precio": 2499.99, "stock": 3, "especificaciones": "16 pulgadas M3", "fecha_ingreso": "2024-01-03"},
]


def make_db():
    """Return a fresh in-memory connection + cursor with the productos table."""
    conn = sqlite3.connect(":memory:")
    cursor = conn.cursor()
    create_table("productos", CREATE_PRODUCTOS, conn, cursor)
    return conn, cursor


# ── Tests ──────────────────────────────────────────────────────────────────────

class TestListTables(unittest.TestCase):

    def test_returns_existing_table(self):
        conn, cursor = make_db()
        self.assertIn("productos", list_tables(conn, cursor))

    def test_empty_db_returns_empty_list(self):
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        self.assertEqual(list_tables(conn, cursor), [])

    def test_sqlite_sequence_excluded(self):
        conn, cursor = make_db()
        # sqlite_sequence is created after first AUTOINCREMENT insert
        populate_table("productos", COLS, [SAMPLE_PRODUCTS[0]], conn=conn, cursor=cursor)
        tables = list_tables(conn, cursor)
        self.assertNotIn("sqlite_sequence", tables)


class TestCreateTable(unittest.TestCase):

    def test_table_is_created(self):
        conn = sqlite3.connect(":memory:")
        cursor = conn.cursor()
        create_table("productos", CREATE_PRODUCTOS, conn, cursor)
        self.assertIn("productos", list_tables(conn, cursor))

    def test_duplicate_create_does_not_raise(self):
        conn, cursor = make_db()
        # calling again should be a no-op
        create_table("productos", CREATE_PRODUCTOS, conn, cursor)
        self.assertIn("productos", list_tables(conn, cursor))


class TestPopulateTable(unittest.TestCase):

    def test_insert_dict_records(self):
        conn, cursor = make_db()
        populate_table("productos", COLS, SAMPLE_PRODUCTS, data_structure="dict", conn=conn, cursor=cursor)
        count = cursor.execute("select count(*) from productos").fetchone()[0]
        self.assertEqual(count, len(SAMPLE_PRODUCTS))

    def test_insert_tuple_records(self):
        conn, cursor = make_db()
        tuples = [tuple(p[c] for c in COLS) for p in SAMPLE_PRODUCTS]
        populate_table("productos", COLS, tuples, data_structure="tuples", conn=conn, cursor=cursor)
        count = cursor.execute("select count(*) from productos").fetchone()[0]
        self.assertEqual(count, len(SAMPLE_PRODUCTS))

    def test_invalid_data_structure_returns_none(self):
        conn, cursor = make_db()
        result = populate_table("productos", COLS, [], data_structure="invalid", conn=conn, cursor=cursor)
        self.assertIsNone(result)


class TestReadTable(unittest.TestCase):

    def setUp(self):
        self.conn, self.cursor = make_db()
        populate_table("productos", COLS, SAMPLE_PRODUCTS, conn=self.conn, cursor=self.cursor)

    def test_read_all_columns(self):
        rows = read_table("productos", cursor=self.cursor)
        self.assertEqual(len(rows), 3)

    def test_read_specific_columns(self):
        rows = read_table("productos", cols=["nombre", "precio"], cursor=self.cursor)
        self.assertEqual(rows[0], ("iPhone 15 Pro", 999.99))

    def test_read_with_filter(self):
        rows = read_table("productos", filter="marca='Apple'", cursor=self.cursor)
        self.assertEqual(len(rows), 2)

    def test_read_with_limit(self):
        rows = read_table("productos", limit=1, cursor=self.cursor)
        self.assertEqual(len(rows), 1)

    def test_read_with_filter_and_limit(self):
        rows = read_table("productos", filter="marca='Apple'", limit=1, cursor=self.cursor)
        self.assertEqual(len(rows), 1)


class TestUpdateRecords(unittest.TestCase):

    def setUp(self):
        self.conn, self.cursor = make_db()
        populate_table("productos", COLS, SAMPLE_PRODUCTS, conn=self.conn, cursor=self.cursor)

    def test_update_with_filter(self):
        update_records("productos", "precio", 799.99, filter="nombre='Galaxy S24'",
                       conn=self.conn, cursor=self.cursor)
        row = self.cursor.execute("select precio from productos where nombre='Galaxy S24'").fetchone()
        self.assertEqual(row[0], 799.99)

    def test_update_all_rows(self):
        update_records("productos", "stock", 0, conn=self.conn, cursor=self.cursor)
        rows = self.cursor.execute("select stock from productos").fetchall()
        self.assertTrue(all(r[0] == 0 for r in rows))


class TestTruncateTable(unittest.TestCase):

    def test_table_is_emptied(self):
        conn, cursor = make_db()
        populate_table("productos", COLS, SAMPLE_PRODUCTS, conn=conn, cursor=cursor)
        truncate_table("productos", conn=conn, cursor=cursor)
        count = cursor.execute("select count(*) from productos").fetchone()[0]
        self.assertEqual(count, 0)

    def test_autoincrement_resets(self):
        conn, cursor = make_db()
        populate_table("productos", COLS, [SAMPLE_PRODUCTS[0]], conn=conn, cursor=cursor)
        truncate_table("productos", conn=conn, cursor=cursor)
        populate_table("productos", COLS, [SAMPLE_PRODUCTS[0]], conn=conn, cursor=cursor)
        row = cursor.execute("select id from productos").fetchone()
        self.assertEqual(row[0], 1)


class TestDropTable(unittest.TestCase):

    def test_table_is_removed(self):
        conn, cursor = make_db()
        drop_table("productos", cursor=cursor)
        self.assertNotIn("productos", list_tables(conn, cursor))


class TestDeleteRecords(unittest.TestCase):

    def setUp(self):
        self.conn, self.cursor = make_db()
        populate_table("productos", COLS, SAMPLE_PRODUCTS, conn=self.conn, cursor=self.cursor)

    def test_delete_with_filter(self):
        delete_records("productos", filter="marca='Apple'", cursor=self.cursor)
        rows = read_table("productos", filter="marca='Apple'", cursor=self.cursor)
        self.assertEqual(len(rows), 0)

    def test_delete_without_filter_returns_none(self):
        result = delete_records("productos", cursor=self.cursor)
        self.assertIsNone(result)

    def test_other_records_unaffected(self):
        delete_records("productos", filter="marca='Apple'", cursor=self.cursor)
        rows = read_table("productos", cursor=self.cursor)
        self.assertEqual(len(rows), 1)
        self.assertEqual(rows[0][2], "Samsung")  # marca column


if __name__ == "__main__":
    unittest.main()
