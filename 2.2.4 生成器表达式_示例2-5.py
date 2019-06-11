import array

symbols='@#$%^&*'

result=tuple(ord(symbol) for symbol in symbols)
print(result)

result1=array.array("I",(ord(symbol) for symbol in symbols))
print(result1)