"""
Запуск тестов для бизнес-логики регистрации пользователей
"""

import pytest
import sys
import os

def main():
    print(" Запуск тестов бизнес-логики регистрации пользователей")
    print(" Используется SQLite in-memory для изолированного тестирования")
    print("=" * 60)
    
    current_dir = os.path.dirname(os.path.abspath(__file__))
    sys.path.insert(0, current_dir)
    
    exit_code = pytest.main([
        "tests/",
        "-v",           # вывод
        "--tb=short",   # короткие tracebacks
        "-s",           # вывод print'ов
        "--color=yes"   # цветной вывод
    ])
    
    print("=" * 60)
    
    if exit_code == 0:
        print(" Все тесты прошли успешно!")
        print(" Бизнес-процесс регистрации пользователей работает корректно")
        print(" Протестированы:")
        print("   - Успешная регистрация пользователя")
        print("   - Защита от дублирования email")
        print("   - Аутентификация пользователя")
        print("   - Изоляция тестовых данных")
    else:
        print(" Некоторые тесты не прошли")
        print(" Требуется анализ проблем в бизнес-логике")
    
    return exit_code

if __name__ == "__main__":
    sys.exit(main())