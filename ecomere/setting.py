from os import getenv
import psycopg2

DB_HOST = getenv("DB_HOST","localhost")
DB_PORT = getenv("DB_PORT",5432)
DB_NAME = getenv("DB_PORT","nbhung")
DB_USER = getenv("DB_PORT","nbhung")
DB_PASSWORD = getenv("DB_PORT","Jecc74h3")

conn = psycopg2.connect(
    database = DB_NAME,
    user = DB_USER,
    password = DB_PASSWORD,
    host = DB_HOST,
    port = DB_PORT
)