import logging
from jsonschema import validate

def ensure_type(value, types, message=None):
    if not isinstance(value, types):
        message = message or 'value: %s must be types: %s' % (value, types)
        raise TypeError(message)


def ensure_in(value, values, message=None):
    if not value in values:
        message = message or 'value: %s must be in values: %s' % (value, values)
        raise ValueError(message)


def ensure_true(value, message=None):
    if not value:
        message = message or 'value: %s must equals True' % value
        raise ValueError(message)


def ensure_safe(func, *args, default=None, **kwargs):
    try:
        return func(*args, **kwargs)
    except Exception as ex:
        logging.exception(ex)
        return default


def ensure_schema(value, schema, message=None):
    validate(value, schema)
