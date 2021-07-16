import pandas

a = list([0 for _ in range(10)] for _ in range(10))
print(pandas.DataFrame(a))