import unittest
from Polynomial import Polynomial


class TestPolynomial(unittest.TestCase):

    def test_init_correct_args(self):
        p = Polynomial([0, 2, 4], [1, 2, 3])
        poly_dict = {0: 1, 2: 2, 4: 3}
        self.assertEqual(p.poly_dict, poly_dict)

    def test_init_empty_list(self):
        self.assertRaises(TypeError, Polynomial, [], [])

    def test_init_no_list(self):
        self.assertRaises(TypeError, Polynomial, "1", b'aadas')

    def test_dimension_mismatch(self):
        self.assertRaises(IndexError, Polynomial, [0, 2, 4], [1, 2])

    def test_init_zero_values_list(self):
        p = Polynomial([0, 0, 0], [0, 0, 0])
        poly_dict = {0: 0}
        self.assertEqual(p.poly_dict, poly_dict)

    def test_init_repeat_values(self):
        p = Polynomial([0, 0, 0, 1, 2], [1, 1, 2, 0, 0])
        poly_dict = {0: 4}
        self.assertEqual(p.poly_dict, poly_dict)

    def test_init_float_values(self):
        p = Polynomial([1.0, 2.0], [1.2, 2.2])
        poly_dict = {1.0: 1.2, 2.0: 2.2}
        self.assertEqual(p.poly_dict, poly_dict)

    def test_eq_true(self):
        p1 = Polynomial([1, 2, 3], [1, 2, 3])
        p2 = Polynomial([1, 2, 3], [1, 2, 3])
        self.assertTrue(p1 == p2)

    def test_eq_false(self):
        p1 = Polynomial([1, 3], [2, 3])
        p2 = Polynomial([1, 2], [1, 2])
        self.assertFalse(p1 == p2)

    def test_eq_other_is_constant(self):
        p1 = Polynomial([0], [0])
        p2 = 0
        self.assertTrue(p1 == p2)

    def test_eq_big_self_other_is_not_polynomial(self):
        p1 = Polynomial([0, 1, 2], [2, 0, 0])
        p2 = 2
        self.assertTrue(p1 == p2)

    def test_eq_other_is_string(self):
        p1 = Polynomial([2, 0, 0], [2, 0, 0])
        self.assertFalse(p1 == "2")

    def test_add_same_polyn_size(self):
        p1 = Polynomial([1, 2], [1, 2])
        p2 = Polynomial([1, 2], [1, 2])
        p3 = p1 + p2
        poly_dict = {1: 2, 2: 4}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_different_polyn_size_first_larger(self):
        p1 = Polynomial([1, 2, 3], [1, 2, 3])
        p2 = Polynomial([1, 2], [1, 2])
        p3 = p1 + p2
        poly_dict = {1: 2, 2: 4, 3: 3}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_different_polyn_size_second_larger(self):
        p1 = Polynomial([1, 2], [1, 2])
        p2 = Polynomial([1, 2, 3], [1, 2, 3])
        p3 = p1 + p2
        poly_dict = {1: 2, 2: 4, 3: 3}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_negative_values(self):
        p1 = Polynomial([0, 1], [1, -1])
        p2 = Polynomial([0, 1], [-1, 1])
        p3 = p1 + p2
        poly_dict = {0: 0}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_left_term_is_const(self):
        p1 = 1
        p2 = Polynomial([0, 1], [1, 2])
        p3 = p1 + p2
        poly_dict = {0: 2, 1: 2}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_zero_values(self):
        p1 = Polynomial([0, 1], [1, 2])
        p2 = Polynomial([0], [0])
        p3 = p1 + p2
        poly_dict = {0: 1, 1: 2}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_positive_constant(self):
        p1 = Polynomial([1, 2], [1, 2])
        p2 = 1
        p3 = p1 + p2
        poly_dict = {0: 1, 1: 1, 2: 2}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_incorrect_constant(self):
        p1 = Polynomial([1, 2], [1, 2])
        self.assertRaises(TypeError, p1.__add__, "ad")

    def test_add_negative_constant(self):
        p1 = Polynomial([0], [1])
        p2 = -1
        p3 = p1 + p2
        poly_dict = {0: 0}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_zero_constant(self):
        p1 = Polynomial([1], [1])
        p2 = 0
        p3 = p1 + p2
        poly_dict = {1: 1}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_positive_float_constant(self):
        p1 = Polynomial([1], [1])
        p2 = 2.4
        p3 = p1 + p2
        poly_dict = {0: 2.4, 1: 1}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_add_zero_degree_polynom(self):
        p1 = Polynomial([1, 2], [1, 2])
        p2 = Polynomial([0], [0])
        p3 = p1 + p2
        poly_dict = {1: 1, 2: 2}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_same_polyn_size(self):
        p1 = Polynomial([2], [2])
        p2 = Polynomial([2], [2])
        p3 = p1 * p2
        poly_dict = {4: 4}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_different_polyn_size(self):
        p1 = Polynomial([0, 1], [1, 2])
        p2 = Polynomial([1], [1])
        p3 = p1 * p2
        poly_dict = {1: 1, 2: 2}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_zero_polyns(self):
        p1 = Polynomial([1, 2], [1, 2])
        p2 = Polynomial([0, 0], [0, 0])
        p3 = p1 * p2
        poly_dict = {0: 0}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_negative_values(self):
        p1 = Polynomial([0, 1], [1, -1])
        p2 = Polynomial([0], [-1])
        p3 = p1 * p2
        poly_dict = {0: -1, 1: 1}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_left_term_is_const(self):
        p1 = 2
        p2 = Polynomial([0, 1], [1, 1])
        p3 = p1 * p2
        poly_dict = {0: 2, 1: 2}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_zero(self):
        p1 = Polynomial([1, 2], [1, 2])
        p2 = 0
        p3 = p1 * p2
        poly_dict = {0: 0}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_float_constant(self):
        p1 = Polynomial([0, 1], [1, 1])
        p2 = 5.4
        p3 = p1 * p2
        poly_dict = {0: 5.4, 1: 5.4}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_one_value_constant(self):
        p1 = Polynomial([0, 1], [1, 1])
        p2 = 1
        p3 = p1 * p2
        poly_dict = {0: 1, 1: 1}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_right_constant(self):
        p1 = Polynomial([0, 1], [1, 1])
        p2 = 5
        p3 = p1 * p2
        poly_dict = {0: 5, 1: 5}
        self.assertEqual(p3.poly_dict, poly_dict)

    def test_mul_incorrect_constant(self):
        p1 = Polynomial([1, 2], [1, 2])
        self.assertRaises(TypeError, p1.__mul__, "5")

    def test_str(self):
        p1 = Polynomial([2, 4], [2, 4])
        self.assertEqual(str(p1), '2*x^2 + 4*x^4')

    def test_str_zero_values(self):
        p1 = Polynomial([0], [0])
        self.assertEqual(str(p1), '0*x^0')

    def test_str_first_float_zero_values(self):
        p1 = Polynomial([0.0, 0.0], [0.0, 0.0])
        self.assertEqual(str(p1), '0*x^0')

    def test_str_first_value_is_negative(self):
        p1 = Polynomial([2, 3], [-1, 1])
        self.assertEqual(str(p1), '-1*x^2 + 1*x^3')

if __name__ == "__main__":
    unittest.main()