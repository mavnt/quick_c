import functools
import inspect
import os
from ctypes import CDLL
from typing import Tuple

from .logging_utils import *
from .utils import get_platform


class quick_c(object):
    def __init__(
        self,
        code: str,
        in_types: Tuple = None,
        out_type: Tuple = None,
        pysetup: str = "",
        skip: bool = False,
    ):
        self.in_types = in_types
        self.out_type = out_type
        self.code = code
        self.pysetup = "from ctypes import *\n" + pysetup if pysetup != "" else None
        self.skip = skip
        self.wrapped_locals = inspect.currentframe().f_back.f_locals

    @staticmethod
    def compile_snippet(c_code: str, f_name: str):
        platform, bits = get_platform()
        log_var(platform)
        log_var(bits)
        compile_command = f"gcc -m{bits} -shared -Wl,-soname,{f_name} -o "
        if platform == "Windows":
            compile_command += f"{f_name}.so -fPIC {f_name}.c"
        elif platform == "Linux":
            compile_command += f"/tmp/{f_name}.so -fPIC {f_name}.c"
        log_var(compile_command)

        with open(f"{f_name}.c", "w") as f:
            f.writelines(c_code)

        os.system(compile_command)
        try:
            os.remove(f"{f_name}.c")
        except FileNotFoundError:
            pass

        def _get_compiled():
            tmp = None
            try:
                if platform == "Windows":
                    tmp = CDLL(f".\\{f_name}.so")
                elif platform == "Linux":
                    tmp = CDLL(f"/tmp/{f_name}.so")
            except Exception as e:
                logging.debug("something went wrong while compiling ")
                logging.debug(e)
            return tmp

        return _get_compiled()

    def execute_setup_code(self):
        logging.debug("----- start of python setup code -----")
        logging.debug(self.pysetup)
        logging.debug("-----  end  of python setup code -----")
        if self.pysetup is not None:
            exec(compile(self.pysetup, "", "exec"), self.wrapped_locals)

    def __call__(self, *args, **kwargs):
        f = args[0]
        if self.skip:
            return f
        library = quick_c.compile_snippet(self.code, f.__name__)
        self.execute_setup_code()
        if library is None:
            return f
        else:
            if hasattr(library, f.__name__):
                c_f = getattr(library, f.__name__)
                if self.in_types is None:
                    arg_types_rest_type = [
                        f.__annotations__[v] for v in f.__annotations__.keys()
                    ]
                    if len(arg_types_rest_type) != 0:
                        c_f.argtypes = arg_types_rest_type[:-1]
                        c_f.restype = arg_types_rest_type[-1]
                else:
                    c_f.argtypes = self.in_types
                    c_f.restype = self.out_type

                @functools.wraps(f)
                def altered_function(*args, **kwargs):
                    return c_f(*args)

                return altered_function
            else:
                raise OSError


if __name__ == "__main__":
    pass
