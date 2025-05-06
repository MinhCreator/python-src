#y = tuple(map(lambda x: x * 2, x)): map(lambda x: x * 2, x): The map() function applies the provided lambda function lambda x: x * 2 to each element of the list x. The lambda function takes a single argument x and returns x * 2, doubling each element of x. The result of the map() function is an iterable containing the doubled elements. This iterable is then converted into a tuple using the tuple() constructor. This creates a new tuple y. So, the output = (2, 4, 6, 8, 10)
"""example"""
x = [1, 2, 3, 4, 5]
y = tuple(map(lambda x: x * 2, x))
print(y)
