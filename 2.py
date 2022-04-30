from functools import wraps
from typing import Callable


def new_functionality_decorator(function: Callable):
    """
    The decorator returns a function that prints "Surprise!" .
    :param function: The function we are to ignore.
    :return: A function which prints "Surprise!".
    """
    @wraps(function)
    def wrapper() -> None:
        """
        The Wrapper prints "surprise!" and does not execute the wrapped function.
        :return:None.
        """
        print("surprise!")
        return None
    return wrapper


@new_functionality_decorator
def original_func() -> None:
    """
    This function is the original function to print "hello world".
    :return: None.
    """
    print("hello world")


if __name__ == "__main__":
    original_func()
