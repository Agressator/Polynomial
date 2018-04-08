
def get_coeffs_from_dict(received_dict):
    coeffs_list = []

    for coeff in received_dict.values():
        coeffs_list.append(coeff)
    return coeffs_list

def replace_coeffs(func):
    def wrapped(*args, **kwargs):
        res_string = func(*args, **kwargs)
        res_string = res_string.replace("1*x", "x")
        res_string = res_string.replace("-1*x", "-x")

        return res_string
    return wrapped

def replace_sign(func):
    def wrapped(*args, **kwargs):
        res_string = func(*args, **kwargs)
        res_string = res_string.replace(" + -", " - ")

        return res_string
    return wrapped

def replace_degrees(func):
    def wrapped(*args, **kwargs):
        res_string = func(*args, **kwargs)
        res_string = res_string.replace("x^1", "x")
        res_string = res_string.replace("*x^0", "")
        res_string = res_string.replace("x^0", "1")

        return res_string
    return wrapped

class Polynomial:
    def __init__(self, coeffs_list):
        if not isinstance(coeffs_list, list):
            raise TypeError('Coefficients must be list')

        if not len(coeffs_list):
            raise TypeError('Coefficients must be not empty')

        self.poly_dict = {0: 0}
        for key in range(len(coeffs_list)):
            if coeffs_list[key] != 0:
                self.poly_dict[key] = coeffs_list[key]

    @replace_coeffs
    @replace_degrees
    @replace_sign
    def __str__(self):
        if self.poly_dict:
            poly_string = ' + '.join('{}*x^{}'.format(coef, degree) for degree, coef in self.poly_dict.items()
                                     if coef != 0)

        if not poly_string:
            return '0'

        return poly_string

    def __add__(self, other):
        if isinstance(other, Polynomial):
            add_poly_dict = {degree: self.poly_dict.get(degree, 0) + other.poly_dict.get(degree, 0)
                    for degree in set(self.poly_dict) | set(other.poly_dict)}
        elif isinstance(other, (float, int)):
            add_poly_dict = self.poly_dict.copy()
            add_poly_dict[0] += other
        else:
            raise TypeError('Operation type error')
        add_coeffs = get_coeffs_from_dict(add_poly_dict)

        return Polynomial(add_coeffs)

    def __radd__(self, other):
        return self + other

    def __sub__(self, other):
        if isinstance(other, Polynomial):
            diff_poly_dict = {degree: self.poly_dict.get(degree, 0) - other.poly_dict.get(degree, 0)
                    for degree in set(self.poly_dict) | set(other.poly_dict)}
        elif isinstance(other, (float, int)):
            diff_poly_dict = self.poly_dict.copy()
            diff_poly_dict[0] -= other
        else:
            raise TypeError('Operation type error')
        diff_coeffs = get_coeffs_from_dict(diff_poly_dict)

        return Polynomial(diff_coeffs)

    def __mul__(self, other):
        mul_coeffs = []

        if isinstance(other, Polynomial):
            for self_coef in self.poly_dict.values():
                for other_coef in other.poly_dict.values():
                    mul_coeffs.append(self_coef * other_coef)
        elif isinstance(other, (float, int)):
            for self_coef in self.poly_dict.values():
                mul_coeffs.append(self_coef * other)
        else:
            raise TypeError('Operation type error')

        return Polynomial(mul_coeffs)

    def __rmul__(self, other):
        return self * other

    def __eq__(self, other):
        if isinstance(other, Polynomial):
            if self.poly_dict == other.poly_dict:
                return True
        elif isinstance(other, (float, int)):
            if self.poly_dict[0] == other:
                return True

        return False

    def __ne__(self, other):
        if isinstance(other, Polynomial):
            if self.poly_dict == other.poly_dict:
                return False
        elif isinstance(other, (float, int)):
            if self.poly_dict[0] == other:
                return False

        return True