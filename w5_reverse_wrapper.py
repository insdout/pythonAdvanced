from functools import wraps


def reversed_dec(func):
    @wraps(func)
    def inner(*arg, **kwargs):
        return func(*arg[::-1], **kwargs)
    return inner
