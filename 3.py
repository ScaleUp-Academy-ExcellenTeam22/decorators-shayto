from functools import wraps
from typing import Callable


def double_decorator(function: Callable):
    """
    The decorator returns a function that prints "hello world!" twice .
    :param function: The function we are to execute
    :return: the function executed twice
    """
    @wraps(function)
    def wrapper() -> None:
        """
        The Wrapper executes the wrapped function twice.
        :return:None.
        """
        function()
        function()
    return wrapper


@double_decorator
def original_func():
    """
    This function is the original function to print "hello world".
    :return: None.
    """
    print("hello world")


def twice(function):
    def wrapper():
        function()
        function()
    return wrapper


if __name__ == "__main__":
    original_func()
