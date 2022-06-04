number = 2520
results = []

while(len(results) != 20):
    for i in range(1, 21):
        if((number % i) == 0):
            results.append(int(number/i))
        else:
            results.clear()
    number += 20
    print(number)

print(str(number))
print(str(results))
