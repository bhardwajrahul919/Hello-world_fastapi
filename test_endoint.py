import unittest  
from fastapi.testclient import TestClient  
from main import app  
  
class TestEndpoint(unittest.TestCase):  
    def setUp(self):  
        self.client = TestClient(app)  
  
    def test_check_number_high(self):  
        response = self.client.get("/check_number/150")  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json(), {"result": "high"})  
  
    def test_check_number_low(self):  
        response = self.client.get("/check_number/50")  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json(), {"result": "low"})  
  
    def test_check_number_equal(self):  
        response = self.client.get("/check_number/100")  
        self.assertEqual(response.status_code, 200)  
        self.assertEqual(response.json(), {"result": "equal"})  
  
if __name__ == '__main__':  
    unittest.main()  
