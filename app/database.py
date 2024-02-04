from .extensions import mysql
import MySQLdb.cursors


def check_primary_key(params):
    cursor = mysql.connection.cursor()

    sql_query = """
    SELECT COUNT(*)
    FROM ClientStatus
    WHERE mac_address LIKE %s
    """

    cursor.execute(sql_query, (params['mac_address'],))

    (count,) = cursor.fetchone()

    mysql.connection.commit()
    cursor.close()
    return count > 0


def create_table(mysql):
    cursor = mysql.connection.cursor()
    cursor.execute(f"USE mysql")

    sql_query = '''
        CREATE TABLE IF NOT EXISTS ClientStatus (
            ip_address VARCHAR(15) NOT NULL,
            mac_address VARCHAR(20) NOT NULL PRIMARY KEY,
            status VARCHAR(10) NOT NULL,
            last_online DATETIME NOT NULL
        ) 
    '''
    
    cursor.execute(sql_query)
    mysql.connection.commit()
    cursor.close()


def insert_client(params):
    cursor = mysql.connection.cursor()

    sql_query = '''
        INSERT INTO ClientStatus (ip_address, mac_address, status, last_online)
        VALUES(%s, %s, %s, %s)
    '''

    cursor.execute(sql_query, (params['ip_address'], 
                               params['mac_address'],
                               params['status'],
                               params['last_online'],)
    )
    mysql.connection.commit()
    cursor.close()


def update_client_status(params):
    cursor = mysql.connection.cursor()

    sql_query = '''
        UPDATE ClientStatus
        SET status = %s, last_online = %s
        WHERE mac_address LIKE %s
    '''

    cursor.execute(sql_query, (params['status'],
                               params['last_online'],
                               params['mac_address'],) 
    )
    mysql.connection.commit()
    cursor.close()


def fetch_clients():
    cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor.execute("SELECT * FROM ClientStatus")
    clients = cursor.fetchall()
    cursor.close()
    return clients


def check_and_update_client_status(app):
    with app.app_context():
        cursor = mysql.connection.cursor()
        
        sql_query = '''
            UPDATE ClientStatus
            SET status = 'offline'
            WHERE status = 'online' AND TIMESTAMPDIFF(MINUTE, last_online, NOW()) >= 5
        '''

        cursor.execute(sql_query)
        mysql.connection.commit()
        cursor.close()