from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


def main():
    driver = webdriver.Chrome()

    try:
        # Переход на сайт
        driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")

        # Ожидание, пока все изображения загрузятся
        wait = WebDriverWait(driver, 10)

        # Ждем, пока все изображения не будут полностью загружены
        images = wait.until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "#image-container img")))

        # Дополнительная проверка, что у всех изображений есть src атрибут
        def all_images_have_src(driver):
            images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")
            if len(images) >= 4:  # Ожидаем как минимум 4 изображения
                return all(img.get_attribute("src") for img in images)
            return False

        wait.until(all_images_have_src)

        # Получаем обновленный список изображений
        images = driver.find_elements(By.CSS_SELECTOR, "#image-container img")

        # Получаем src третьей картинки (индекс 2)
        third_image_src = images[2].get_attribute("src")

        print(f"SRC третьей картинки: {third_image_src}")

    except Exception as e:
        print(f"Произошла ошибка: {e}")

    finally:
        driver.quit()


if __name__ == "__main__":
    main()
