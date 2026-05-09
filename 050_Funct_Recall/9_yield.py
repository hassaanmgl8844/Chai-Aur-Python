# ✏️ Write a generator function called count_up that yields numbers from 1 to 5 one by one!
# next() → 1
# next() → 2
# next() → 3
# next() → 4
# next() → 5


def count_up():
    yield 1
    yield 2
    yield 3
    yield 4
    yield 5


gen = count_up()
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
print(next(gen))
