num = 1000

numPow = 2 ** num
digits = str(numPow)
print(numPow)
total = 0

for i in range(len(digits)):
    total += int(digits[i])
    
print(total)

while True:
    print