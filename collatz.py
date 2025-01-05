def collatz(num):
    if num == 1:
        return 1
    elif num % 2 == 0:
        return num // 2
    elif num % 2 == 1:
        return 3 * num + 1

collatzNum = 0

print('Welcome to the Collatz Machine.')        
print('Enter number:')

while True:
    number = input()

    try:
        int(number)
    except ValueError:
        print('Please enter a valid integer.')
        continue
    break

while number != 1:
    number = collatz(int(number))    
    print(str(number))
    collatzNum += 1

print('Collatz number: ' + str(collatzNum))
