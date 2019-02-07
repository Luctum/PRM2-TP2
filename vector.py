from pydash import py_

vector = []


def compare(a, b):
    real_a = py_.lower_case(py_.deburr(a))
    real_b = py_.lower_case(py_.deburr(b))
    return real_a == real_b and 1 or 0


def create_vector(dictionary, comparatee):
    for element in dictionary:
        value = compare(element, comparatee)
        vector.append(value)


create_vector(['1', '2', 'e', 'é', '10'], '1')
print(vector)
