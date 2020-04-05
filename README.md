# quick_c
Write your (simple) C code within a Python decorator.

## Usage
Write your C code as in the examples.
Use either type annotation or `in_types`, `out_types` kwargs. You need `gcc`.

## Examples

### Add
```python
@quick_c(
    code="""
        int add(int a, int b){
            return a+b;
        }"""
)
def add(a: c_int, b: c_int) -> c_int:
    raise NotImplementedError

print(add(1, 2))
```

### Fibonacci
```python
@quick_c(
    in_types=[c_int],
    out_type=c_int,
    code="""
    #include <stdio.h>
    int fibonacci(int i){
      if (i < 0) return -1;
      if (i == 0) return 0;
      else if (i == 1) return 1;
      else return fibonacci(i-1) + fibonacci(i-2);
    }
    """,
)
def fibonacci(*args):
    raise NotImplementedError

print(fibonacci(30))
```

For more see `quick_c/examples`.
