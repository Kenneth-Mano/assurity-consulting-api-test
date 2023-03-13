import requests
import unittest

class AssurityApiTest(unittest.TestCase):
    
    def setUp(self):
        """This sets up the test by calling the API"""
        self.url = ' https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
        self.response = requests.get(self.url)

    def test_name_is_carbon_credits(self):
        """This test verifies that the name of the API is Carbon credits"""
        self.assertEqual(self.response.json()["Name"], "Carbon credits", msg="API Name is not \"Carbon credits\".")

    def test_can_relist_is_true(self):
        """This test verifies that the CanRelist property of the API is true"""
        self.assertTrue(self.response.json()["CanRelist"], msg="CanRelist is not true.")

    def test_text_of_gallery_description(self):
        """This test verifies that the Promotions element with the name 'Gallery' has a Description that contains the text 'Good position in category'"""
        promotions = self.response.json()["Promotions"]
        for promotion in promotions:
            if promotion["Name"] == "Gallery":
                self.assertIn(promotion["Description"], "Good position in category", msg="Promotions element with the name 'Gallery' does not contain the text 'Good position in category'.")

if __name__ == '__main__':
    unittest.main()