import time 

def ChamperownesConst(rangeN):
    string = "0."
    for i in range(1, rangeN + 1):
        string += str(i)
    return [n for n in string[2:]]

const = ChamperownesConst(1000000)
expression = int(const[0]) * int(const[9]) * int(const[99]) * int(const[999]) * int(const[9999]) * int(const[99999]) * int(const[999999])
print(expression, time.process_time())
