# What is amstrong number?
# 3899  = 3^4 + 8^4 + 9^4 + 9^4      (We are taking 4 because there are 4 digits)
#if this is equal then its AMSTRONG NUMBER otherwise its not
#example of amstrong number is 153 order = 3  1^3+5^3+3^3  1+125+27 =

number = int(input("Enter the number to check if its amstrong or not :"))
order = len(str(number))
# print(order)
copyNumber  = number

sum = 0
while(number>0):
    digit = number%10
    sum+= digit**order
    number = number//10

if (sum == copyNumber):
    print(f"Your number{copyNumber} is an amstrong")
else:
    print(f"Your number{copyNumber} is not an amstrong")