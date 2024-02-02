"""Test docstring for sphinx_test"""


def fake_function(some_arg: int = 0) -> None:
    """
    Test docstring for fake_function.
    :param some_arg: Arbitrary integer.
    :type some_arg: int
    :return: None"""

    print(str(some_arg))
