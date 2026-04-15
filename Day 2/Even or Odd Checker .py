a=float(input("Enter thr first number:"))#take the number from the user
b=float(input("Enter thr second number:"))#take the number from the user
print("="*20)
print(" calculator")
print("="*20)
print(f" {a} + {b} = {a+b}")
print(f" {a} - {b} = {a-b}")
print(f" {a} * {b} = {a*b}")
print(f" {a} / {b}={round(a/b,2)}")
print(f" {a} // {b} = {a//b}")
print(f" {a} %  {b} = {a%b}")
print(f" {a} **  {b} = {a**b}")
print("="*20)



print(f"\n-------comparison---------")
print(f"is a>b? {a>b}")
print(f"is a==b?{a==b}")
print(f"are both positive? {a>0 and b>0}")