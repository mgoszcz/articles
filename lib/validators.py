from inspect import getcallargs

from decorator import decorator


class Validators:

    @staticmethod
    def attribute_validator(argument_name, *types):

        @decorator
        def wrapper(func, *args, **kwargs):

            func_args = getcallargs(func, *args, **kwargs)

            if argument_name not in func_args:
                raise KeyError(f'{argument_name} is not a part of {func.__name__} signature')

            if func_args[argument_name] and not isinstance(func_args[argument_name], types):
                raise TypeError(
                    f'Attribute: {argument_name} has a wrong type! Provided: {type(func_args[argument_name])}. Expected: {types}')

            return func(*args, **kwargs)

        return wrapper
