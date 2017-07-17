import MySQLdb

def connection():
    conn = MySQLdb.connect(host='localhost', user='root', passwd = 'tobe2013', db = 'pythonprogramming')
    c = conn.cursor()

    return c, conn
