import allure
import pytest
from selenium import webdriver
from .calculator_page import CalculatorPage


@allure.feature("Калькулятор")
@allure.severity(allure.severity_level.CRITICAL)
class TestSlowCalculator:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.driver = webdriver.Chrome()
        self.calculator_page = CalculatorPage(self.driver)
        yield
        self.driver.quit()

    @allure.title("Тест вычисления выражения с задержкой 45 секунд")
    @allure.description("Проверка работы калькулятора с установленной "
                        "задержкой вычислений 45 секунд. "
                        "Вычисление выражения 7+8")
    def test_slow_calculator_45_seconds(self):
        """
        Тестирует процесс расчёта выражений с установленным временем ожидания.
        Действия:
        1. Открытие страницы калькулятора.
        2. Задание задержки вычислений.
        3. Расчёт выражения '7 + 8'.
        4. Ожидание отображения результата.
        5. Проверка полученного результата.

        :return: None
        """

        with allure.step("Открытие страницы калькулятора"):
            self.calculator_page.open()

        with allure.step("Установка задержки на 45 секунд"):
            self.calculator_page.set_delay(45)

        with allure.step("Выполнение расчёта выражения '7 + 8'"):
            self.calculator_page.calculate_expression("7+8")

        with allure.step("Ожидание появления результата 15 на экране"):
            self.calculator_page.wait_until_result_is(15)

        with allure.step("Проверка итогового результата"):
            actual_result = int(self.calculator_page.get_result())
            assert actual_result == 15, (
                f"Expected '15', but got {actual_result}")