import pytest

def test_successful_user_registration(user_service):
    """Тест успешной регистрации пользователя"""
    print("🔧 Подготовка теста: Успешная регистрация")
    
    # Arrange
    email = "test@example.com"
    name = "Иван Иванов"
    password = "password123"
    
    # Act
    user = user_service.register_user(email, name, password)
    
    # Assert
    assert user is not None, "Пользователь не должен быть None"
    assert user['email'] == email, f"Email должен быть {email}"
    assert user['full_name'] == name, f"Имя должно быть {name}"
    assert user['is_active'] == 1, "Пользователь должен быть активен"
    
    print(" Тест пройден: Пользователь успешно зарегистрирован")

def test_duplicate_email_registration(user_service):
    """Тест регистрации с дублирующимся email"""
    print("🔧 Подготовка теста: Дублирование email")
    
    # Первая регистрация
    user_service.register_user("duplicate@example.com", "User One", "pass1")
    
    # Вторая регистрация с тем же email
    with pytest.raises(ValueError) as exc_info:
        user_service.register_user("duplicate@example.com", "User Two", "pass2")
    
    assert "уже существует" in str(exc_info.value), "Должна быть ошибка дублирования"
    print(" Тест пройден: Корректная обработка дублирования email")

def test_user_authentication(user_service):
    """Тест аутентификации пользователя"""
    print("🔧 Подготовка теста: Аутентификация")
    
    # Регистрируем пользователя
    user_service.register_user("auth@example.com", "Test User", "correct_password")
    
    # Успешная аутентификация
    user = user_service.authenticate_user("auth@example.com", "correct_password")
    assert user is not None, "Аутентификация должна быть успешной"
    assert user['email'] == "auth@example.com", "Email должен совпадать"
    
    # Неуспешная аутентификация
    user = user_service.authenticate_user("auth@example.com", "wrong_password")
    assert user is None, "Аутентификация с неверным паролем должна вернуть None"
    
    print(" Тест пройден: Аутентификация работает корректно")

def test_database_isolation(user_service):
    """Тест изоляции базы данных между тестами"""
    print("🔧 Подготовка теста: Изоляция базы данных")
    
    # В этом тесте база должна быть пустой (из-за изоляции фикстур)
    users = user_service.get_all_users()
    assert len(users) == 0, "База данных должна быть пустой в начале теста"
    
    # Регистрируем пользователя
    user_service.register_user("isolation@example.com", "Isolation Test", "password")
    
    # Проверяем, что пользователь добавлен
    users = user_service.get_all_users()
    assert len(users) == 1, "Должен быть ровно один пользователь"
    
    print(" Тест пройден: Изоляция базы данных работает")