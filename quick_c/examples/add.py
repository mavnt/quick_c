from ctypes import *

from ..quick_c import quick_c


@quick_c(
    code="""
        int add1(int a, int b){
            return a+b;
        }"""
)
def add1(a: c_int, b: c_int) -> c_int:
    raise NotImplementedError


@quick_c(
    code="""
        int add2(int a, int b){
            return a+b;
        }""",
    skip=True,
)
def add2(a: c_int, b: c_int) -> c_int:
    print("skip=True")
    return a + b


if __name__ == "__main__":
    print(add1(1, 2))
    print(add2(1, 2))
