numbers = []

with open("series.txt", "r") as file:
    data = file.read().replace("\n", "")
    for char in data:
        numbers.append(int(char))
count = len(numbers)
products = []
for i in range(len(numbers)):
    product = numbers[i]
    for adjacent in range(1, 13):
        if((i + adjacent) < count):
            product *= numbers[i + adjacent]
    products.append(product)

print(str(products))
print(str(max(products)))

