num = int(input("Enter any number: "))
flag = 0

# Numbers less than or equal to 1 are not prime
if num <= 1:
    flag = 1
else:
    # Check for factors up to num // 2
    for i in range(2, (num // 2) + 1):
        if (num % i == 0):  # Fixed the syntax error here by adding 'i'
            flag = 1
            break

if (flag == 1):
    print("Not prime")
else:
    print("Prime")
