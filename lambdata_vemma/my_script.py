
from pandas import DataFrame
from lambdata_vemma.my_mod import enlarge

print('Hello')

df = DataFrame({"a":[1,2,3,], "b":[4,5,6]})
print(df.head())

x = 12
print(enlarge(x))
