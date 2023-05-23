class InvalidCodeException(Exception):
    pass


def validate_code(code):
    if len(code) < 32:
        raise InvalidCodeException

    if len(code) > 32:
        raise InvalidCodeException

    
