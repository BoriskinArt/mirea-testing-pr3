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

    def test_convert_miles_to_dm(self):
        self.assertEqual(main.Data(1).convert_miles_to_dm(), 16093.4)

    def test_convert_miles_to_cm(self):
        self.assertEqual(main.Data(1).convert_miles_to_cm(), 160934)

    def test_convert_miles_to_mm(self):
        self.assertEqual(main.Data(1).convert_miles_to_mm(), 1609340)

    def test_convert_inch_to_km(self):
        self.assertEqual(main.Data(1).convert_inch_to_km(), 0.000025)

    def test_convert_inch_to_m(self):
        self.assertEqual(main.Data(1).convert_inch_to_m(), 0.025)

    def test_convert_inch_to_dm(self):
        self.assertEqual(main.Data(1).convert_inch_to_dm(), 0.25)

    def test_convert_inch_to_cm(self):
        self.assertEqual(main.Data(1).convert_inch_to_cm(), 2.54)

    def test_convert_inch_to_mm(self):
        self.assertEqual(main.Data(1).convert_inch_to_mm(), 25.4)

    def test_convert_ft_to_km(self):
        self.assertEqual(main.Data(1).convert_ft_to_km(), 0.0003)

    def test_convert_ft_to_m(self):
        self.assertEqual(main.Data(1).convert_ft_to_m(), 0.3)

    def test_convert_ft_to_dm(self):
        self.assertEqual(main.Data(1).convert_ft_to_dm(), 3.05)

    def test_convert_ft_to_cm(self):
        self.assertEqual(main.Data(1).convert_ft_to_cm(), 30.48)

    def test_convert_ft_to_mm(self):
        self.assertEqual(main.Data(1).convert_ft_to_mm(), 304.8)


if __name__ == '__main__':
    unittest.main()