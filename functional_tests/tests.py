from selenium import webdriver
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_check_title_site(self):
        # Херцог захотел узнать какие же ачивки или статьи есть у Люка.
        # Он заходит на домашнюю страницу сайта
        self.browser.get("http://localhost:8000")

        # Он замечает, что на заголовок у страницы "Home | sadchordoma"
        self.assertIn("Home | sadchordoma", self.browser.title)

        # Он видит, что на главной странице есть статьи, кликнув на которые он
        # переходит на страницу отдельной статьи


if __name__ == "__main__":
    unittest.main()
