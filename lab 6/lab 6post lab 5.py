#Ahuja Slock 

num = input("Enter number: ")
if len(num) == 1:
    print(num)
else:
    print(num[-1] + num[1:-1] + num[0])
