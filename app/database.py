import os
from flask_mysqldb import MySQL

#class Database(MySQL):
    

mysql = MySQL()


def init_db(app):
    app.config['MYSQL_HOST'] = os.environ.get('MYSQL_HOST')
    app.config['MYSQL_USER'] = os.environ.get('MYSQL_USER')
    app.config['MYSQL_PASSWORD'] = os.environ.get('MYSQL_PASSWORD')
    app.config['MYSQL_DB'] = os.environ.get('MYSQL_DATABASE')
    mysql.init_app(app)
    

def __execute_query__(sql_query, data=None, fetch=None):
    result = None
    cursor = mysql.connection.cursor()
    cursor.execute(f"USE mysql")
    cursor.execute(sql_query, data)
    mysql.connection.commit()

    if fetch == 'all':
        result = cursor.fetchall()
    elif fetch == 'one':
        (result,) = cursor.fetchone()
        
    cursor.close()
    return result


def check_primary_key(params):
    sql_query = "SELECT COUNT(*) FROM ClientStatus WHERE mac_address = %s"
    data = (params['mac_address'],)
    count = __execute_query__(sql_query, data, "one") 
    return count and count > 0


def insert_client(params):
    sql_query = "\
        INSERT INTO ClientStatus (ip_address, mac_address, status, last_online)\
        VALUES(%s, %s, %s, %s)"

    data = (params['ip_address'], 
            params['mac_address'],
            params['status'],
            params['last_online'],)

    __execute_query__(sql_query, data)


def update_client_status(params):
    sql_query = "\
        UPDATE ClientStatus\
        SET status = %s, last_online = %s\
        WHERE mac_address LIKE %s"

    data = (params['status'],
            params['last_online'],
            params['mac_address'],) 

    __execute_query__(sql_query, data)


def fetch_clients():
    sql_query = "SELECT * FROM ClientStatus"
    clients = __execute_query__(sql_query, fetch="all")
    return clients


def check_and_update_client_status():
    sql_query = "UPDATE ClientStatus SET status = 'offline'\
                    WHERE status = 'online' AND TIMESTAMPDIFF(MINUTE, last_online, NOW()) >= 5"
    __execute_query__(sql_query)

