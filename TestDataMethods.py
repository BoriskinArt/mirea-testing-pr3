import unittest
import main
 
 
class TestDataMethods(unittest.TestCase):
    def test_convert_km_to_m(self):
        self.assertEqual(main.Data(1).convert_km_to_m(), 1000)
        self.assertEqual(main.Data(-1).convert_km_to_m(), 0)
 
    def test_convert_km_to_dm(self):
        self.assertEqual(main.Data(1).convert_km_to_dm(), 100)
 
    def test_convert_km_to_cm(self):
        self.assertEqual(main.Data(1).convert_km_to_cm(), 100000)
 
    def test_convert_km_to_mm(self):
        self.assertEqual(main.Data(1).convert_km_to_mm(), 1000000)
 
    def test_convert_m_to_km(self):
        self.assertEqual(main.Data(1000).convert_m_to_km(), 1)
 
    def test_convert_m_to_dm(self):
        self.assertEqual(main.Data(1000).convert_m_to_dm(), 10000)
 
    def test_convert_m_to_cm(self):
        self.assertEqual(main.Data(1).convert_m_to_cm(), 100)
 
    def test_convert_m_to_mm(self):
        self.assertEqual(main.Data(1).convert_m_to_mm(), 1000)
 
    def test_convert_dm_to_km(self):
        self.assertEqual(main.Data(10000).convert_dm_to_km(), 1)
 
    def test_convert_dm_to_m(self):
        self.assertEqual(main.Data(10).convert_dm_to_m(), 1)
 
    def test_convert_dm_to_cm(self):
        self.assertEqual(main.Data(1).convert_dm_to_cm(), 10)
 
    
if __name__ == '__main__':
    unittest.main()