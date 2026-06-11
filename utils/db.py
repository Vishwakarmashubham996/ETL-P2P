
import pyodbc
from hdbcli import dbapi

def get_hana_conn(cfg):
    return dbapi.connect(**cfg)

def get_sql_conn(conn_str):
    return pyodbc.connect(conn_str)
