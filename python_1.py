def calc():
    a = 12
    b = 22

    def add():
        c = a + b
        print("Sum is",c)

    def sub():
        c = a - b
        print("Sub is",c)

    return add, sub

'''
func_1,func_2 = calc()
func_1()
func_2()
'''

functions = calc()
# call add
functions[0]()
# call sub
functions[1]()






