from ctypes import *

from ..quick_c import quick_c


@quick_c(
    code="""
#include <inttypes.h>
#include <stdlib.h>
uint64_t* prime_sieve (uint64_t limit, uint64_t* length) {
    uint64_t* primes = calloc (limit + 1, sizeof (uint64_t));
    uint64_t* result = calloc (limit + 1, sizeof (uint64_t));
    uint64_t p, i, last;
    for (p = 2; p * p <= limit; p++)
        if (primes[p] == 0)
            for (i = p * 2; i <= limit; i += p)
                primes[i] = 1;
    for (i = 2, last = 0; i <= limit; i++)
        if (primes[i] == 0)
            result[last++] = i;

    *length = last;
    return result;
}"""
)
def prime_sieve(n: c_uint64, length: POINTER(c_uint64)) -> POINTER(c_uint64):
    raise NotImplementedError


if __name__ == "__main__":
    size = c_uint64(0)
    a = prime_sieve(10000, pointer(size))
    print(a[: size.value])
