from selenium import webdriver
import unittest

class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Chrome()

    def tearDown(self):
        self.browser.quit()

    def test_can_start_a_list_and_retrieve_it_late(self):
        # The test function goes to checl the homw page of a new online to-do app.
        self.browser.get('http://127.0.0.1:8000/')

        # the page title and header mention to-do lists
        self.assertIn('To-Do', self.browser.title)
        self.fail('Finish the test!')

        # test app is invited to enter a to-do item straight away
        # she types ....


if __name__=='__main__':
    unittest.main(warnings='ignore')