from ctypes import *

from ..quick_c import quick_c


@quick_c(
    pysetup="""
size = c_int()
p = pointer(size)""",
    code="""
#include <stdlib.h>
#include <math.h>
int* divisors_of (int n, int* length) {
    int* c = calloc ((int) (2 * sqrt (n)), sizeof (int));
    int i, last = 0;
    for (i = 2; i < n; i++)
        if (n % i == 0)
            c[last++] = i;
    *length = last;
    return c;
}""",
)
def divisors_of(n: c_int, lenght: POINTER(c_int)) -> POINTER(c_int):
    return NotImplementedError


if __name__ == "__main__":
    a = divisors_of(100, p)
    print(a[: size.value])
