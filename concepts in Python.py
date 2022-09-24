"""
number = 1
while number < 5:
    print(number)
    number +=1
    """



"""
counter = 26
while counter > 15:
    print(counter)
    counter -= 2

print("while loop has ended")
"""

"""
cars = ['audit', 'vw', 'jaguar', 'mini']
for x in cars:
    
    if x == "jaguar":
        continue

    print(x)
"""
"""
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print(i*2)
"""

"""
numbers = [1, 2, 3, 4, 5, 6]
for i in numbers:
    print(i)
    if i == 7:
        break
    print("inside the for loop")
else:
    print("outside the for loop")
"""
"""
counter = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in counter:
    if x % 2:
        pass
    else:
        print(x)
"""

"""
numbers = [1, 2, 3]
letters = ['a', 'b', 'c']
for number in numbers:
    for letter in letters:
     print(number, letter)
    
"""
"""
var = 1
while var == 1:
    print(var)
"""

"""

def print_name(f_name = 'nadia'):
    print("my name is : " + f_name)

print_name()
"""

"""
def multiple(num1, num2):
    return num1*num2

result=multiple(2,3)
print("result = {}".format(result))
"""
"""
def greeting(name):
    return "hello, " + name

result = greeting("nadia")
print(result)
"""


def about_me():
    name = "nadia"
    age = 25
    children = 0
    return [name, age, children]

result = about_me()
print(result)



























































































