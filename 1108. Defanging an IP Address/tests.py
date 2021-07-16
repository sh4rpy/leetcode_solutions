from unittest import TestCase

from solution import Solution


class SolutionTestCase(TestCase):
    def test_solution(self) -> None:
        obj = Solution()
        ip1 = '1.1.1.1'
        ip2 = '255.100.50.0'
        self.assertEqual(obj.defangIPaddr(ip1), '1[.]1[.]1[.]1')
        self.assertEqual(obj.defangIPaddr(ip2), '255[.]100[.]50[.]0')
