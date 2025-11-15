import sqlite3
import hashlib

class DatabaseManager:
    def __init__(self, database_url=":memory:"):
        self.database_url = database_url
        self.conn = None
        self._connect()
        self.create_tables()
    
    def _connect(self):
        """Установка соединения с базой данных"""
        self.conn = sqlite3.connect(self.database_url)
        self.conn.row_factory = sqlite3.Row
    
    def create_tables(self):
        """Создание таблиц"""
        cursor = self.conn.cursor()
        cursor.execute('''
            CREATE TABLE IF NOT EXISTS users (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                email TEXT UNIQUE NOT NULL,
                full_name TEXT NOT NULL,
                hashed_password TEXT NOT NULL,
                is_active BOOLEAN DEFAULT 1,
                created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
            )
        ''')
        self.conn.commit()
    
    def execute(self, query, params=()):
        """Выполнение SQL запроса"""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        self.conn.commit()
        return cursor
    
    def fetch_one(self, query, params=()):
        """Получение одной строки"""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchone()
    
    def fetch_all(self, query, params=()):
        """Получение всех строк"""
        cursor = self.conn.cursor()
        cursor.execute(query, params)
        return cursor.fetchall()
    
    def close(self):
        """Закрытие соединения"""
        if self.conn:
            self.conn.close()