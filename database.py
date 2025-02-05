import sqlite3

class Database:
    def __init__(self):
        self.conn = sqlite3.connect('apontamento.db')
        self.cursor = self.conn.cursor()
        self.create_table()

    def create_table(self):
        self.cursor.execute('''
            CREATE TABLE IF NOT EXISTS apontamento (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                data TEXT,
                turno TEXT,
                processo TEXT,
                maquina TEXT,
                referencia TEXT,
                refugo TEXT,
                producao INTEGER,
                defeitos TEXT,
                scrap_type TEXT,
                timestamp DATETIME DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()

    def insert_data(self, data, turno, processo, maquina, referencia, refugo, producao, defect, scrap_type):
        self.cursor.execute('''
            INSERT INTO apontamento (data, turno, processo, maquina, referencia, refugo, producao, defeitos, scrap_type)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (data, turno, processo, maquina, referencia, refugo, producao, defect, scrap_type))
        self.conn.commit()

    def get_last_registrations(self, limit):
        query = "SELECT data, turno, processo, maquina, referencia, refugo, producao, defeitos FROM apontamento ORDER BY id DESC LIMIT ?"
        self.cursor.execute(query, (limit,))
        return self.cursor.fetchall()
    
    def read_data(self):
        query = "SELECT * FROM apontamento ORDER BY id DESC"
        self.cursor.execute(query)
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()