from pydash import py_


def compare(a, b):
    reala = py_.lower_case(py_.deburr(a))
    realb = py_.lower_case(py_.deburr(b))
    return reala == realb and 1 or 0

