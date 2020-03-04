import logging
from functools import wraps

logger = logging.getLogger(__name__)
formater = logging.Formatter('%(asctime)s %(name)-12s %(levelname)-8s %(message)s')
logger.setLevel(logging.INFO)


def exception_logging(value):
    def decorator(f):
        @wraps(f)
        def wrapper(*args, **kwargs):
            try:
                return f(*args, **kwargs)
            except Exception as e:
                logger.error("异常: {}".format(str(e)))
                return value

        return wrapper

    return decorator
