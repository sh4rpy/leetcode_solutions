from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def setUp(self) -> None:
        self.instance = Solution()

    def test_solution(self) -> None:
        ip1 = '1.1.1.1'
        ip2 = '255.100.50.0'
        self.assertEqual(self.instance.defangIPaddr(ip1), '1[.]1[.]1[.]1')
        self.assertEqual(self.instance.defangIPaddr(ip2), '255[.]100[.]50[.]0')
