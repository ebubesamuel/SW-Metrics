import time
import unittest

from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


class TestHorizontalSlider(unittest.TestCase):

    """horizontal_slider
    http://the-internet.herokuapp.com/horizontal_slider"""
    
    def setUp(self):
        self.driver = webdriver.Chrome(ChromeDriverManager().install())
       # self.driver = webdriver.Safari()
        self.base_url = "http://the-internet.herokuapp.com/horizontal_slider"
        self.driver.maximize_window()
        time.sleep(5)
        self.driver.get(self.base_url)
        time.sleep(2)
        self.assertIn(self.base_url, self.driver.current_url)
        self.slider = self.driver.find_element(By.CSS_SELECTOR, ".sliderContainer > input:nth-child(1)")
        self.assertTrue(self.slider)
        self.slider.click()

    def test_horizontal_slider(self):
        "test_horizontal_slider"
        driver = self.driver
        for _ in range(10):
            self.slider.send_keys(Keys.ARROW_RIGHT)
        driver.save_screenshot("horizontal_slider.png")

    def test_horizontal_slider_arrow_up(self):
        "test_horizontal_slider arrow-up"
        driver = self.driver
        self.slider.send_keys(Keys.ARROW_UP)
        driver.save_screenshot("horizontal_slider_up.png")

    def tearDown(self):
        srange = self.driver.find_element(By.ID, "range")
        self.assertNotEqual(srange.text, "0")
        time.sleep(5)
        self.driver.close()


if __name__ == '__main__':
    unittest.main(
        # defaultTest="TestHorizontalSlider.test_horizontal_slider_arrow_left"
    )