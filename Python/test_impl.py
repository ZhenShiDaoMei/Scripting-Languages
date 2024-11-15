import unittest
import impl
from impl import PhysicalInfo

class TestPhysicalInfo(unittest.TestCase):
    def setUp(self):
        self.physical_info = PhysicalInfo()

    #tests for name
    def test_valid_name(self):
        valid_names = ["Jason Wu", "Abid Malik", "joe momma", "A B"]
        for name in valid_names:
            with self.subTest(name=name):
                try:
                    self.physical_info.set_name(name)
                except ValueError:
                    self.fail(f"set_name ValueError: {name}")
    def test_invalid_name(self):
        invalid_names = ["", "337", "CSE_337", "A", "sbu", "@Jane", "S_B_U"]
        for name in invalid_names:
            with self.subTest(name=name):
                with self.assertRaises(ValueError):
                    self.physical_info.set_name(name)

    #tests for gender
    def test_valid_gender(self):
        valid_genders = ["M", "F"]
        for gender in valid_genders:
            with self.subTest(gender=gender):
                try:
                    self.physical_info.set_gender(gender)
                except ValueError:
                    self.fail(f"set_gender ValueError: {gender}")
    def test_invalid_gender(self):
        invalid_genders = ["Male", "", "0", "f", "MF", "both"]
        for gender in invalid_genders:
            with self.subTest(gender=gender):
                with self.assertRaises(ValueError):
                    self.physical_info.set_gender(gender)

    #tests for height
    def test_valid_height(self):
        for height in range(17, 85):
            with self.subTest(height=height):
                try:
                    self.physical_info.set_height(height)
                except ValueError:
                    self.fail(f"set_height ValueError: {height}")
    def test_invalid_height(self):
        invalid_heights = [16, 85, 0, -1, "20", "twenty inches", None]
        for height in invalid_heights:
            with self.subTest(height=height):
                with self.assertRaises(ValueError):
                    self.physical_info.set_height(height)

    #tests for temp
    def test_valid_temperature(self):
        valid_temperatures = [95.0, 99.9, 101.1, 104.0]
        for temp in valid_temperatures:
            with self.subTest(temp=temp):
                try:
                    self.physical_info.set_temperature(temp)
                except ValueError:
                    self.fail(f"set_temperature ValueError: {temp}")
    def test_invalid_temperature(self):
        invalid_temperatures = [94.9, 97, 104.1, "98.6", None]
        for temp in invalid_temperatures:
            with self.subTest(temp=temp):
                with self.assertRaises(ValueError):
                    self.physical_info.set_temperature(temp)

    #tests for date
    def test_valid_date(self):
        valid_dates = ["01-01-1900", "09-09-1999", "12-8-2023", "12-31-2100"]
        for date in valid_dates:
            with self.subTest(date=date):
                try:
                    self.physical_info.set_date(date)
                except ValueError:
                    self.fail(f"set_date ValueError: {date}")
    def test_invalid_date(self):
        invalid_dates = ["12-31-1899", "1900-01-01", "01-1900-01", "20-20-2020",  "01-01-2101", ""]
        for date in invalid_dates:
            with self.subTest(date=date):
                with self.assertRaises(ValueError):
                    self.physical_info.set_date(date)

if __name__ == '__main__':
    unittest.main()