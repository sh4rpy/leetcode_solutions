from unittest import TestCase

from solution import SubrectangleQueries


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = SubrectangleQueries([[1, 2, 1], [4, 3, 4], [3, 2, 1], [1, 1, 1]])
        obj.updateSubrectangle(0, 0, 3, 2, 5)
        obj.updateSubrectangle(3, 0, 3, 2, 10)
        self.assertEqual(obj.rectangle, [None, 1, None, 5, 5, None, 10, 5])

        obj = SubrectangleQueries([[1, 1, 1], [2, 2, 2], [3, 3, 3]])
        obj.updateSubrectangle(0, 0, 2, 2, 100)
        obj.updateSubrectangle(1, 1, 2, 2, 20)
        self.assertEqual(obj.rectangle, [None, 1, None, 100, 100, None, 20])
