import requests
import unittest

class AssurityApiTest(unittest.TestCase):
    
    def setUp(self):
        self.url = ' https://api.tmsandbox.co.nz/v1/Categories/6327/Details.json?catalogue=false'
        self.response = requests.get(self.url)

    def test_name_is_carbon_credits(self):
        self.assertEqual(self.response.json()["Name"], "Carbon credits")

    def test_can_relist_is_true(self):
        self.assertTrue(self.response.json()["CanRelist"])

    def test_text_of_gallery_description(self):
        promotions = self.response.json()["Promotions"]
        for promotion in promotions:
            if promotion["Name"] == "Gallery":
                self.assertIn(promotion["Description"], "Good position in category")

if __name__ == '__main__':
    unittest.main()