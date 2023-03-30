import unittest
import Functions5

class TestFunctions5(unittest.TestCase):
    def test_distance_between_points(self):
        self.assertEqual(Functions5.distance_between_points(17, 11, 42, 31), "The distance between the points is: 12.529964086141668")
        self.assertEqual(Functions5.distance_between_points(-22, 0, 16, -1), "The distance between the points is: 27.80287754891569")

    def test_most_frequent_letter(self):
        self.assertEqual(Functions5.most_frequent_letter("Greatsword"), "The most frequent letter in 'greatsword' is 'r', which appears 2 times.")
        self.assertEqual(Functions5.most_frequent_letter("Wikipedia"), "The most frequent letter in 'wikipedia' is 'i', which appears 3 times.")

    def test_sum_of_naturals(self):
        self.assertEqual(Functions5.sum_of_naturals(5), 15)
        self.assertEqual(Functions5.sum_of_naturals(27), 378)
        self.assertEqual(Functions5.sum_of_naturals(100), 5050)

    def test_sumdigto1(self):
        self.assertEqual(Functions5.sumdigto1(14), 5)
        self.assertEqual(Functions5.sumdigto1(677), 2)
        self.assertEqual(Functions5.sumdigto1(197456), 5)

    def test_sum_of_squares(self):
        self.assertEqual(Functions5.sum_of_squares(4), 30)
        self.assertEqual(Functions5.sum_of_squares(22), 3795)
        self.assertEqual(Functions5.sum_of_squares(144), 1005720)


if __name__ == '__main__':
        unittest.main()