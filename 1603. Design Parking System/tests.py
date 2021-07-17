from unittest import TestCase

from solution import ParkingSystem


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        actual = []
        obj = ParkingSystem(1, 1, 0)
        actual.append(obj.addCar(1))
        actual.append(obj.addCar(2))
        actual.append(obj.addCar(3))
        actual.append(obj.addCar(1))
        self.assertEqual(actual, [True, True, False, False])
