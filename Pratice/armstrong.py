num=int(input("Enter the number : "))
p =len(str(num))
sum=0
n=num
while (num >0):
    sum += (num % 10)**p
    num = num//10
if (n==sum):
    print("armstrong number")
else:
    print("Number is not armstrong")
