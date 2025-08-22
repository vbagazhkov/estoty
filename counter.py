import unittest
from alttester import AltDriver, By


class TestCounter(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        cls.driver = AltDriver()   #
        cls.driver.load_scene("SampleScene")

    @classmethod
    def tearDownClass(cls):
        cls.driver.stop()

    def test_initial_value_is_zero(self):
        counter_text = self.driver.find_object(By.NAME, "CountText")  
        self.assertEqual(counter_text.get_text(), "0")

    def test_button_increments_value(self):
        button = self.driver.find_object(By.NAME, "Submitted")
        button.tap()
        counter_text = self.driver.find_object(By.NAME, "CountText")
        self.assertEqual(counter_text.get_text(), "1")

    def test_value_does_not_exceed_ten(self):
        button = self.driver.find_object(By.NAME, "Submitted")
        for _ in range(15):
            button.tap()
        counter_text = self.driver.find_object(By.NAME, "CountText")
        self.assertEqual(counter_text.get_text(), "10")


if __name__ == '__main__':
    unittest.main()
