from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import NoSuchElementException

def main():
    driver = webdriver.Chrome()
    driver.get("https://ru.wikipedia.org/wiki/%D0%97%D0%B0%D0%B3%D0%BB%D0%B0%D0%B2%D0%BD%D0%B0%D1%8F_%D1%81%D1%82%D1%80%D0%B0%D0%BD%D0%B8%D1%86%D0%B0")

    while True:
        user_input = input("Введите запрос: ")
        if user_input.lower() == "выйти":
            break

        driver.find_element(By.NAME, "search").send_keys(user_input)
        driver.find_element(By.NAME, "search").send_keys(Keys.ENTER)

        while True:
            action = input(
                "Выберите действие:\n"
                "1. Листать параграфы текущей статьи\n"
                "2. Перейти на одну из связанных страниц\n"
                "3. Выйти из программы\n"
                "Введите номер действия: "
            )

            if action == "1":
                pass
            elif action == "2":
                links = driver.find_elements(By.CSS_SELECTOR, "a.mw-redirect")
                if links:
                    for i, link in enumerate(links):
                        print(f"{i+1}. {link.text}")
                    while True:
                        link_choice = input(
                            "Выберите номер страницы для перехода: "
                        )
                        try:
                            selected_link = links[int(link_choice) - 1]
                            selected_link.click()
                            break
                        except (IndexError, ValueError):
                            print("Неверный номер страницы.")
                else:
                    print("На странице нет ссылок.")
            elif action == "3":
                break
            else:
                print("Неверный номер действия.")

    driver.quit()

if __name__ == "__main__":
    main()