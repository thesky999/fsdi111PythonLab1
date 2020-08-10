print('Hello from Python')

last_name = 'Dotzler'
age = 32
found = False
total = 13.44

print(last_name)
print("Trevor " + last_name)

# this will throw error
print(last_name + ' ' + str(age))
print(age + total)

# math
print(1 + 1)
print(234 - 987)
print(345 * 345)
print(78 / 3)

# if
print(' ---------------------------------------- ')
if(age < 99):
    print('You are still young')
    print('this is inside the if')
print('this is outside the if')


print('  ----------------------------------')

if(total > 100):
    print("You will get free shipping")
elif(total > 50):
    print('You need to pay half of the shipping price')
else:
    print("You need to pay for shipping")

def say_hi():
    print('Hi from a function')
    print('still inside the fn')

say_hi() # calling the fn
say_hi()