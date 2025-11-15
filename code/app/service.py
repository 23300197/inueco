import hashlib

class UserService:
    def __init__(self, db_manager):
        self.db = db_manager
    
    def _hash_password(self, password):
        """Хеширование пароля"""
        return hashlib.sha256(password.encode()).hexdigest()
    
    def register_user(self, email, full_name, password):
        """Регистрация пользователя"""
        # Проверка существующего пользователя
        existing = self.db.fetch_one('SELECT id FROM users WHERE email = ?', (email,))
        if existing:
            raise ValueError(f"Пользователь с email {email} уже существует")
        
        # Хеширование пароля
        hashed_password = self._hash_password(password)
        
        # Создание пользователя
        cursor = self.db.execute(
            'INSERT INTO users (email, full_name, hashed_password) VALUES (?, ?, ?)',
            (email, full_name, hashed_password)
        )
        
        # Получение созданного пользователя
        user = self.db.fetch_one('SELECT * FROM users WHERE id = ?', (cursor.lastrowid,))
        return dict(user) if user else None
    
    def get_user_by_email(self, email):
        """Поиск пользователя по email"""
        user = self.db.fetch_one('SELECT * FROM users WHERE email = ?', (email,))
        return dict(user) if user else None
    
    def authenticate_user(self, email, password):
        """Аутентификация пользователя"""
        user = self.get_user_by_email(email)
        if user and user['hashed_password'] == self._hash_password(password):
            return user
        return None
    
    def get_all_users(self):
        """Получение всех пользователей (для тестов)"""
        users = self.db.fetch_all('SELECT * FROM users')
        return [dict(user) for user in users]