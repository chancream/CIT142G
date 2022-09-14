def accumulator():
  total = 0
  value = None
  while True:
    value = yield total
    if value is None: break
    total = total + (value + 3)
generator = accumulator()
print(next(generator))
print(generator.send(5))
print(generator.send(10))