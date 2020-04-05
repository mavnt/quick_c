from ctypes import *

from ..quick_c import quick_c


@quick_c(
    in_types=[c_int],
    out_type=c_int,
    code="""
    #include <stdio.h>
    int fibonacci1(int i){
      if (i < 0) return -1;
      if (i == 0) return 0;
      else if (i == 1) return 1;
      else return fibonacci1(i-1) + fibonacci1(i-2);
    }
    """,
)
def fibonacci1(*args):
    raise NotImplementedError


@quick_c(
    in_types=[c_int],
    out_type=c_int,
    code="""
    #include <stdio.h>
    int fibonacci2(int i){
      if (i < 0) return -1;
      if (i == 0) return 0;
      else if (i == 1) return 1;
      else return fibonacci2(i-1) + fibonacci2(i-2);
    }
    """,
)
def fibonacci2(a: c_int) -> c_int:
    raise NotImplementedError


if __name__ == "__main__":
    print(fibonacci1(30))
    print(fibonacci2(30))
