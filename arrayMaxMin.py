
#cretae array and find max min


arr=[10,34,45,6,20,25,19]
min=arr[0]
max=arr[0]

for num in arr:
    if num<min:
        smin=min
        min=num
    if num <max:
        smax=max
        max= num

print("minimum :",min)
print("Maximum :",max)
print("econd minimum :", min)
print("Second maxmium : ", max)
