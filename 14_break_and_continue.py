print("Break: ")
count = 1
while count<=5:
    print(count)
    count+=1;
    if(count==4):
        break;

print("Continue: ")
number = 1
while number<=5:
    if(number==4):
        number+=1
        continue
    print(number)
    number+=1
    