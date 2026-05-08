def fib_count(n, count_ref=None):
    if count_ref is None:
        count_ref = {"calls": 0}
    count_ref["calls"] += 1

    if n <= 1:
        return n
    return fib_count(n - 1, count_ref) + fib_count(n - 2, count_ref)

for n in [5, 6, 7]:
    count_ref = {"calls": 0}
    result = fib_count(n, count_ref)
    print(f"fib({n}) = {result}, calls = {count_ref['calls']}")