from selenium import webdriver
from selenium.webdriver.common.by import By
import unittest


class NewVisitorTest(unittest.TestCase):
    def setUp(self) -> None:
        self.browser = webdriver.Chrome()

    def tearDown(self) -> None:
        self.browser.quit()

    def test_home_page_title(self):
        # Херцог захотел узнать какие же ачивки или статьи есть у Люка.
        # Он заходит на домашнюю страницу сайта
        self.browser.get("http://localhost:8000")

        # Он замечает, что на заголовок у страницы "Home | sadchordoma"
        self.assertIn("Home | sadchordoma", self.browser.title)

    def test_home_page_blog_has_articles_look_correct(self):
        # Он видит, что на главной странице есть статьи, кликнув на которые он
        # переходит на страницу отдельной статьи
        self.browser.get("http://localhost:8000")
        article1 = self.browser.find_element(By.CLASS_NAME, "article")
        article_summary1 = self.browser.find_element(By.CLASS_NAME, "article-summary")
        self.assertTrue(article1)
        self.assertTrue(article_summary1)


if __name__ == "__main__":
    unittest.main()
