# Q1/Write a method that will remove any given character from a String?

string = "aiDojo"
print(string.replace("D",""))

# Q2/Write a program to find all prime numbers up to a given range
# of numbers?

x = int(input("Enter the first number: "))
y = int(input("Enter the second number: "))

for Numbers in range(x, y):
      if Numbers > 1:
           for i in range(2,Numbers):  
               if (Numbers % i) == 0:
                       break
           else:
               print(Numbers)

# Q3/write a function that count how many the given character repeated
# in a given string?

def setCount():
      string = input("Enter any string: ")
      character = input("Enter the character: ")
      count = 0
      for i in string:
           if i == character:
                 count+= 1
      return print("The count is :",count)   

setCount()