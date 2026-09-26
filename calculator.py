# Simple Calculator - By Deepak

print("Calculator - Add, Subtract, Multiply, Divide")

num1 = float(input("Pehla number daal: "))
num2 = float(input("Dusra number daal: "))

print("1. Jod (+) \n2. Ghatav (-) \n3. Guna (*) \n4. Bhaag (/)")
choice = input("Kya karna hai? 1/2/3/4 daal: ")

if choice == '1':
    print(f"Result: {num1 + num2}")
elif choice == '2':
    print(f"Result: {num1 - num2}")
elif choice == '3':
    print(f"Result: {num1 * num2}")
elif choice == '4':
    print(f"Result: {num1 / num2}")
else:
    print("Galat choice!")
