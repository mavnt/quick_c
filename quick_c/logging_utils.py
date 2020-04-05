PROJECT_NAME = "quick_c"
LEVEL = "INFO"
try:
    import colorlog

    handler = colorlog.StreamHandler()
    handler.setFormatter(
        colorlog.ColoredFormatter(
            "%(log_color)s%(levelname)-8s: %(message)-100s[%(module)s:%(lineno)d]"
        )
    )

    logging = colorlog.getLogger(PROJECT_NAME)
    logging.setLevel(LEVEL)
    logging.addHandler(handler)
except ModuleNotFoundError:
    import logging

    logging.basicConfig(
        format="%(levelname)-8s: %(message)-100s[%(module)s:%(lineno)d]"
    )
    logging = logging.getLogger(PROJECT_NAME)
    logging.setLevel(LEVEL)


def log_var(var):
    import inspect

    caller_locals: dict = inspect.currentframe().f_back.f_locals
    if len(set(caller_locals.keys())) != len(set(caller_locals.values())):
        logging.warn("More than one local var with same value !!!")
    items = [(k, caller_locals[k]) for k in caller_locals if caller_locals[k] == var]
    for item in items:
        k, v = item
        logging.debug(f"{k} => {v}; type({k}) => {type(v)}")
