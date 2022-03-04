import unittest
from list_rotation import rotate
from parameterized import parameterized


class TestListRotation(unittest.TestCase):

    @parameterized.expand([
        [['a', 'b', 'c', 'd', 'e', 'f'], 0, ['a', 'b', 'c', 'd', 'e', 'f']],
        [['a', 'b', 'c', 'd', 'e', 'f'], 1, ['f', 'a', 'b', 'c', 'd', 'e']],
        [['a', 'b', 'c', 'd', 'e', 'f'], 2, ['e', 'f', 'a', 'b', 'c', 'd']],
        [['a', 'b', 'c', 'd', 'e', 'f'], 3, ['d', 'e', 'f', 'a', 'b', 'c']],
        [['a', 'b', 'c', 'd', 'e', 'f'], 4, ['c', 'd', 'e', 'f', 'a', 'b']],
    ])
    def test_an_assertion_is_raised_for_an_invalid_opacity_value(self, my_list, num_rotations, expected_result):

        self.assertEqual(rotate(my_list, num_rotations),
                         expected_result)


if __name__ == '__main__':
    unittest.main()
