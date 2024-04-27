import unittest
from code import weekday_name, weekday, calendar, transform_calendar

class TestWeekdayName(unittest.TestCase):
    def test_weekday_name(self):
        self.assertEqual(weekday_name(3), 'thu')
        self.assertEqual(weekday_name(0), 'mon')
        self.assertEqual(weekday_name(6), 'sun')
        self.assertEqual(weekday_name(2), 'wed')
        self.assertEqual(weekday_name(5), 'sat')

    def test_weekday_name_invalid(self):
        with self.assertRaises(AssertionError):
            weekday_name(7)
        with self.assertRaises(AssertionError):
            weekday_name(-1)
        with self.assertRaises(AssertionError):
            weekday_name(8)
        with self.assertRaises(AssertionError):
            weekday_name(-2)

class TestWeekday(unittest.TestCase):
    def test_weekday(self):
        self.assertEqual(weekday("12.08.2015"), 2)
        self.assertEqual(weekday("28.02.2016"), 6)
        self.assertEqual(weekday("01.01.2016"), 4)
        self.assertEqual(weekday("01.01.2017"), 6)
        self.assertEqual(weekday("01.01.2018"), 0)

    def test_weekday_invalid(self):
        with self.assertRaises(AssertionError):
            weekday("12.08.201")
        with self.assertRaises(AssertionError):
            weekday("28.02.201")
        with self.assertRaises(AssertionError):
            weekday("01.01.201")
        with self.assertRaises(AssertionError):
            weekday("01.01.20")

class TestCalendar(unittest.TestCase):
    def test_calendar(self):
        self.assertEqual(calendar(8, 2015), 'mon tue wed thu fri sat sun\n                      1   2\n  3   4   5   6   7   8   9\n 10  11  12  13  14  15  16\n 17  18  19  20  21  22  23\n 24  25  26  27  28  29  30\n 31')
        self.assertEqual(calendar(5, 2002), 'mon tue wed thu fri sat sun\n                          1   2   3   4   5\n  6   7   8   9  10  11  12\n 13  14  15  16  17  18  19\n 20  21  22  23  24  25  26\n 27  28  29  30  31')
        self.assertEqual(calendar(1, 2017), 'mon tue wed thu fri sat sun\n                          1   2   3   4   5\n  6   7   8   9  10  11  12\n 13  14  15  16  17  18  19\n 20  21  22  23  24  25  26\n 27  28  29  30  31')

    def test_calendar_invalid(self):
        with self.assertRaises(AssertionError):
            calendar(13, 2015)
        with self.assertRaises(AssertionError):
            calendar(0, 2015)
        with self.assertRaises(AssertionError):
            calendar(8, 1583)
        with self.assertRaises(AssertionError):
            calendar(8, 1582)

class TestTransformCalendar(unittest.TestCase):
    def test_transform_calendar(self):
        self.assertEqual(transform_calendar(calendar(5, 2002)), 'mon   6 13 20 27\ntue   7 14 21 28\nwed 1 8 15 22 29\nthu 2 9 16 23 30\nfri 3 10 17 24 31\nsat 4 11 18 25\nsun 5 12 19 26')
        self.assertEqual(transform_calendar(calendar(8, 2015)), 'mon   3 10 17 24 31\ntue   4 11 18 25\nwed   5 12 19 26\nthu   6 13 20 27\nfri   7 14 21 28\nsat 1 8 15 22 29\nsun 2 9 16 23 30')
        self.assertEqual(transform_calendar(calendar(1, 2017)), 'mon   2 9 16 23 30\ntue   3 10 17 24 31\nwed   4 11 18 25\nthu   5 12 19 26\nfri   6 13 20 27\nsat 7 14 21 28\nsun 1 8 15 22 29')

if __name__ == '__main__':
    unittest.main()
