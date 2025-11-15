import pytest
import sys
import os

# Добавляем корневую директорию проекта в Python path
current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.dirname(current_dir)
sys.path.insert(0, parent_dir)

from app.database import DatabaseManager
from app.service import UserService

@pytest.fixture
def db_manager():
    """Фикстура для менеджера базы данных"""
    manager = DatabaseManager(":memory:")  # Таблицы создаются автоматически в __init__
    yield manager
    manager.close()

@pytest.fixture
def user_service(db_manager):
    """Фикстура для сервиса пользователей"""
    return UserService(db_manager)