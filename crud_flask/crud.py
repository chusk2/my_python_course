# # Creación de un *CRUD* con `sqlite3` (intermedio)

import sqlite3
from pathlib import Path
import os

# ## Establecer directorio de trabajo

PROJECT_HOME_FOLDER = '/home/daniel/code/my_python_course/sqlite_crud'

if os.getcwd() == PROJECT_HOME_FOLDER:
    os.chdir(PROJECT_HOME_FOLDER + "/data/")

# ## Funciones auxiliares


# Crearé algunas funciones auxiliares que me permitan realizar algunas tareas que ayuden en las tareas de mantenimiento de la base de datos y sus tablas.

### Listado de tablas de la BD
# Esta función devuelve una lista de las tablas que contiene la BD de la conexión activa.

def list_tables(conn, cursor):
    tables = (cursor
              .execute("SELECT name FROM sqlite_master WHERE type='table'")
              .fetchall()
    )
    tables = [i[0] for i in tables if i[0] != "sqlite_sequence"]
    return tables

## Iniciar conexión  
def init_connection(db_file : str) -> tuple[sqlite3.Connection, sqlite3.Cursor] | None :
    # check if file exists
    if (Path(".") / db_file).exists():
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            print("Connection created successfuly!")
            return conn, cursor
        except Exception as e:
            print(f"Error: {e}")
            return None
    else:
        print(f"{db_file} does not exist. I will create it.")
        try:
            conn = sqlite3.connect(db_file)
            cursor = conn.cursor()
            print("Connection created successfuly!")
            print(f"Database file created: {db_file}")
            return conn, cursor
        except Exception as e:
            print(f"Error: {e}")
            return None


## C (create)

# ### Creación de tabla
# Esta función crea una tabla a partir de una *query* con el código SQL de creación de la tabla.

def create_table(table_name, query, conn, cursor):
    try:
        # check if table exists
        if not table_name in list_tables(conn, cursor):
            cursor.execute(query)
            conn.commit()

            # get the database list
            db_details = conn.execute("PRAGMA database_list").fetchall()
            db_name = db_details[0][2].split("/")[-1]

            # success message
            print(f"Table {table_name} was successfuly created at database {db_name}!")
        
        # table was already created
        else:
            print(f"Table {table_name} already exists. No actions were taken.")
    except Exception as e:
        print(f"Error: {e}")

### Inserción de datos
def populate_table(table, cols, values, onn, cursor, data_structure="dict"):
    
    try:
        # check if data_structure value is valid:
        if data_structure not in ["tuples", "dict"]:
            print("Invalid data_structure value: must be tuples or dict!")
            return None
        
        # create a dictionary containing column names as keys
        # and values contained in each tuple provided in values
        
        if data_structure != "dict":
            values = [{k:v for k,v in zip(cols, t)}
                    for t in values]
        
        # create placeholders
        placeholders = []
        for c in cols:
            placeholders.append(f":{c}")
        placeholders = ", ".join(placeholders)

        
        insert_query = f'''
        insert into {table} ({", ".join(cols)})
        values ({placeholders}) ;
        '''

        # insert records into db
        cursor.executemany(insert_query, values)
        conn.commit()
        
        # check if insertion was ok
        records_count_in_values = len(values)
        records_count_in_table= cursor.execute(f"select count(*) from {table} ;").fetchone()[0]

        if records_count_in_table == records_count_in_values:
            print(f"Insertion succesful. {records_count_in_table} records where inserted!")
        else:
            print("Something went wrong!")
            print(f"Count of provided values: {records_count_in_values}")
            print(f"Count of provided values: {records_count_in_table}")
            conn.rollback()
    
    except Exception as e:
        print(f"Error: {e}")

## R (read)

### Lectura de datos

def read_table(table, cursor, cols="*", filter = None, limit = None):
    try:
        if cols != "*":
            columns = ", ".join(cols)
        else:
            columns = "*" 
        query = f'''
        select {columns}
        from {table}
        '''
        if filter:
            query += f"\n\twhere {filter}"
        
        if limit:
            query += f"\nlimit {limit}"
        
        query += " ;"

        return cursor.execute(query).fetchall()
    
    except Exception as e:
        print(f"Error: {e}")

## U (update)

### Actualización de registros

def update_records(table, col, value, conn, cursor, filter = ""):
    try:
        query = f'''
        update {table}
        set {col} = {value}
        '''
        if filter:
            query += "\n\twhere {filter}"
        
        query += "\n ;"

        cursor.execute(query)
        conn.commit()
        
    except Exception as e:
        print(f"Error: {e}")

## D (delete)

### Eliminación


# #### Vaciado de la tabla

def truncate_table(table, conn, cursor):
    try:
        cursor.execute(f"delete from {table} ;")
        
        # reset the id values
        cursor.execute(f'delete from sqlite_sequence where name ="{table}" ;')
        conn.commit()
        print(f"Table \"{table}\" has been cleaned from all records.")
        
    except Exception as e:
        print(f"Error: {e}")
    

#### Eliminación de la tabla

def drop_table(table, conn, cursor):
    try:
        cursor.execute(f"drop table {table} ;")

        # check if table has been removed from db
        tables_list = cursor.execute("SELECT name FROM sqlite_master WHERE type='table'").fetchall()
        tables_list = [i[0] for i in tables_list]
        
        if table not in tables_list:
            conn.commit()
            print(f"Table \"{table}\" has been removed from the database!")
        else:
            print(f'Table "{table}" could not be removed from database.')
            
    except Exception as e:
        print(f"Error: {e}")

#### Eliminación de registros

def delete_records(table, conn, cursor, filter = ""):
    try:
        if not filter:
            print("A filter is needed to perform selective deletion of records.")
            return None
        
        query = f"delete from {table} where {filter} ;"
        
        cursor.execute(query)
    
    except Exception as e:
        print(f"Error: {e}")




