#This is a program for converting any base number to any other base number
number=input("enter the number")
given_base=int(input("enter the base of given number"))
target_base=int(input("enter the base to convert the number"))
def given_to_decimal(number, given_base):
    decimal_number=0
    for num in number:
        if "0"<=num<="9":
            value=ord(num)-ord("0")
        else:
            value=ord(num.upper())-ord("A")+10
            
        if value>=given_base:
            return "invalid number for the given base"
            
        decimal_number=decimal_number*given_base+value
    return decimal_number

def decimal_to_target(decimal_number, target_base):
    if decimal_number==0:
        return "0"
    target_number=""
    while decimal_number>0:
        remainder=decimal_number%target_base
        if remainder<10:
            target_number=chr(remainder+ord("0"))+target_number
        else:
            target_number=chr(remainder-10+ord("A"))+target_number
        decimal_number//=target_base
    return target_number
def convert_base(number, given_base, target_base):
        decimal_number=given_to_decimal(number, given_base)
        target_number=decimal_to_target(decimal_number, target_base)
        return target_number

result=convert_base(number, given_base, target_base)
print(f"the number {number} in base {given_base} is equal to {result} in base {target_base}")

