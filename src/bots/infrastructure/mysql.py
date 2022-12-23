from ...mysql.connect import ConnectionMysql

class MysqlBots:
    def __init__(self):
        self.connect = ConnectionMysql()

    def statusBots(self):
        cursor = self.connect.cursor
        cursor.execute( "SELECT DISTINCT name,tx_status,date FROM tb_status_bots ORDER BY date DESC LIMIT 2")        
        dt = cursor.fetchall()
        self.connect.conn.close()
        return dt