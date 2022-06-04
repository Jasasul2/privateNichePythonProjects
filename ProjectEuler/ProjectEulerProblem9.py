ax = 1
bx = 1
cx = 1

def VerifyTriplet(a, b, c):
    if(a ** 2 + b ** 2 == c ** 2):
        return True
    return False

def GetTriplet():
    for c in range (1, 1000):
        for b in range(1, c):
            for a in range(1, b):
                if(VerifyTriplet(a, b, c)):
                    print("")
                    print("Triplet: " + str(a) + " " + str(b) + " " + str(c))
                    if((a + b + c) == 1000):
                        ax = a
                        bx = b
                        cx = c
                        return

GetTriplet()
print("correct triplet is " + str(ax) + " " + str(bx) + " " + str(cx))
