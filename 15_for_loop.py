list = [1, 2, 3, 4, 5, 6, 7, 8]

for el in list:
    print(el)
else:
    print("END")
    
tup = (1, 2, 3, 4, 5, 6, 7, 8)
for el in tup:
    print(el)
else:
    print("END")
    
# range function returns a sequence of numbers, starting from 0 by default, and
# increments by 1 by default and stops before  specified number
# range(start, stop, step)
for el in range(1, 10, 2):
    print(el)
    
for el in range(0,5):
    print(el)

for el in range(3):
    print(el)