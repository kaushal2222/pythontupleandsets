def main():
 a = int(input("Enter a value for first number "))
 b = int(input("Enter a value for second number "))
 b, a = a, b
 print("After Swapping")
 print(f"Value for first number {a}")
 print(f"Value for second number {b}")
if __name__ == "__main__":
  main()
