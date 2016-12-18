#https://www.udemy.com/automate/learn/v4/t/lecture/3470582

def boxPrint(symbol, width, height):
    print(symbol * width)
    for i in range(height -2):
        print(symbol+(' '*(width-2))+symbol)
    print(symbol * width)

boxPrint('*',10,5)

