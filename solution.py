import requests
import unittest

class AssurityApiTest(unittest.TestCase):
    
    def setUp(self):
        """This sets up the test by calling the API"""
        self.url = ' https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
        self.response = requests.get(self.url)

    def test_name_is_carbon_credits(self):
        """This test verifies that the name of the API is Carbon credits"""
        value = self.response.json()["Name"]
        self.assertEqual(value, "Carbon credits", msg=f"API Name is {value}, which is not \"Carbon credits\".")

    def test_can_relist_is_true(self):
        """This test verifies that the CanRelist property of the API is true"""
        value = self.response.json()["CanRelist"]
        self.assertTrue(value, msg=f"CanRelist has the value {value}, which is not equal to true.")

    def test_text_of_gallery_description(self):
        """This test verifies that the Promotions element with the name 'Gallery' has a Description that contains the text 'Good position in category'"""
        promotions = self.response.json()["Promotions"]
        for promotion in promotions:
            if promotion["Name"] == "Gallery":
                value = promotion["Description"]
                self.assertIn(value.lower(), "good position in category", msg=f"The Promotions element with the name 'Gallery' has a 'Description' with the text {value}, which does not contain the text 'good position in category'.")

if __name__ == '__main__':
    unittest.main()