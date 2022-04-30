from functools import wraps
from typing import Callable

"""
Decorator factory.
The factory receives an argument and a type, and returns a decorator that 
validates that the argument that was received is from the correct type.
If yes, the factory returns the decorated function. If not, it raise a TypeError exception.
"""


def decorator_factory(correct_type: type):
    """
    The decorator factory receives a variable type.
    If the function receives an argument which is not from the received type, a TypeError exception raised.
    If not, it returns the decorated function.
    :param correct_type: The wanted argument type.
    :return: The decorator function.
    :raise: TypeError: if type of received argument is not the correct_type.
    """

    def decorator(function: Callable):
        """
        The decorator returns a function wrapped in a validation function.
        :param function: The function we want to wrap.
        :return: function - function wrapped in type validation.
        :raise: TypeError: If the argument is not from the defined correct_type.
        """

        @wraps(function)
        def wrapper(value: object) -> object:
            """
            The wrapper returns the return value of the received functions if its argument's type is the correct type.
            :param value: The functions' argument.
            :return: the functions return value.
            :raise TypeError: if the received argument's type is not as the defined correct_type.
            """
            if type(value) == correct_type:
                return function(value)
            raise TypeError
        return wrapper
    return decorator


@decorator_factory(int)
def type_check(value: int) -> None:
    """
    The function prints the given value.
    Iff the argument's type is not an int, it raises a TypeError exception.
    :param value: The value we want to print.
    :return: None
    :raise: TypeError: If the argument passed to the decorator function is not the correct type.
    """
    print("The type of the value is correct! Here is the value:", value)


if __name__ == "__main__":
    try:
        type_check([3, 4, 5])
    except TypeError:
        print("Type error- the argument is not the correct type")
