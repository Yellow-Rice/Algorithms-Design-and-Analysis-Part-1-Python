x = 'x'
y = 'y'

def func1():
    x = 'a'

def func2():
    global y
    y = 'b'

func1()
func2()

print('x =', x)
print('y =', y)
