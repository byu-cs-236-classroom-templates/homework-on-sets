# src/setops.py

# ✅ Correct implementation
def union(a: set[int], b: set[int]) -> set[int]:
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    if not all(isinstance(x, int) for x in a | b):
        raise TypeError("All elements of the sets must be integers")
    return a | b

# ❌ Incorrect implementation (uses intersection)
def intersection(a: set[int], b: set[int]) -> set[int]:
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    if not all(isinstance(x, int) for x in a | b):
        raise TypeError("All elements of the sets must be integers")
    return a | b

# ❌ Incorrect implementation (repeats a)
def cartesian_product_version_1(a: set[int], b: set[int]) -> set[tuple[int,int]]:
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    
    return {(x, y) for x in a for y in a}

# ❌ Incorrect implementation returns a set of sets instead of set of tuples
def cartesian_product_version_2(a: set[int], b: set[int]) -> set:
    if not isinstance(a, set) or not isinstance(b, set):
        raise TypeError("Arguments must be sets")
    
    return {{x, y} for x in a for y in b}
