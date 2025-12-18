import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from calculator_page import CalculatorPage


class TestSlowCalculator(unittest.TestCase):

    def setUp(self):
        """Настройка перед каждым тестом"""
        # Настройка ChromeDriver с помощью webdriver-manager
        service = Service(ChromeDriverManager().install())
        self.driver = webdriver.Chrome(service=service)
        self.driver.maximize_window()

        # Создание экземпляра Page Object
        self.calculator = CalculatorPage(self.driver)

        # Открытие страницы калькулятора
        self.driver.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")

    def test_slow_calculator_addition(self):
        """Тест операции сложения с задержкой 45 секунд"""
        # Шаг 1: Установка задержки 45 секунд
        self.calculator.set_delay("45")

        # Шаг 2: Выполнение операции 7 + 8
        self.calculator.perform_addition()

        # Шаг 3: Проверка результата
        result = self.calculator.get_result()
        self.assertEqual("15", result,
                         "Результат операции 7 + 8 должен быть 15")


    def tearDown(self):
        """Действия после каждого теста"""
        if self.driver:
            self.driver.quit()