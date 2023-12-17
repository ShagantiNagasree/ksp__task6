#python program
num1=10
num2=20
def add(a,b):
     print("sum of ",a," and ",b," is : ",a+b)
def sub(a,b):
     print("subtraction between ",a," and ",b," is : ",a-b)
def mul(a,b):
    print("multiplication of ",a," and ",b," is : ",a*b)
def div(a,b):
    print("division of ",a," and ",b," is : ",a/b)
add(20,29)
sub(30,40)
mul(4,5)
div(25,9)

#if statements
time=int(input("enter time in 24 hours format : "))
if(time<=12):
     print("good morning")
elif(time<=15):
     print("good afternoon")
elif(time<=16):
     print("good evening")
else:
     print("good night")
     
# for loop
n=int(input("enter the number for which you want to see  multiplication table : "))  
for i in range(1,11):
     print(n," * ",i," = ",n*i)  


#WHILE LOOP
n=int(input("enter the number for which you want to see  multiplication table : ")) 
while(n<=10):
     print(n," * ",i," = ",n*i) 


