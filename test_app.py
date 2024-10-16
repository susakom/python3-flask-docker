import unittest
from app import app

class BasicTests(unittest.TestCase):

    def setUp(self):
        # Создаем тестовый клиент приложения
        self.app = app.test_client()
        self.app.testing = True

    def test_home(self):
        # Проверяем, что домашняя страница доступна (возвращает статус 200)
        response = self.app.get('/')
        self.assertEqual(response.status_code, 200)

if __name__ == "__main__":
    unittest.main()
