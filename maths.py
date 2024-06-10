import math

def add(x, y):
  """Adds two numbers."""
  return x + y

def subtract(x, y):
  """Subtracts two numbers."""
  return x - y

def multiply(x, y):
  """Multiplies two numbers."""
  return x * y

def divide(x, y):
  """Divides two numbers (handles division by zero)."""
  if y == 0:
    return "Error: Cannot divide by zero."
  else:
    return x / y

def square(x):
  """Squares a number."""
  return x * x

def square_root(x):
  """Calculates the square root of a number (handles negative input)."""
  if x < 0:
    return "Error: Cannot take square root of negative number."
  else:
    return math.sqrt(x)

def sine(x):
  """Calculates the sine of an angle in radians."""
  return math.sin(math.radians(x))

def cosine(x):
  """Calculates the cosine of an angle in radians."""
  return math.cos(math.radians(x))

def tangent(x):
  """Calculates the tangent of an angle in radians (handles division by zero)."""
  if math.cos(math.radians(x)) == 0:
    return "Error: Cannot take tangent at 90 degrees or 270 degrees."
  else:
    return math.tan(math.radians(x))

def main():
  """Main function for interactive calculator use."""
  print("Welcome to the Simple Calculator!")

  while True:
    print("\nAvailable operations:")
    print("  1. Add")
    print("  2. Subtract")
    print("  3. Multiply")
    print("  4. Divide")
    print("  5. Square")
    print("  6. Square Root")
    print("  7. Sine (in degrees)")
    print("  8. Cosine (in degrees)")
    print("  9. Tangent (in degrees)")
    print("  0. Exit")

    choice = input("Enter your choice (1-9 or 0 to exit): ")

    if choice in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9'):
      if choice == '0':
        print("Exiting calculator.")
        break

      # Get numbers
      try:
        num1 = float(input("Enter the first number: "))
        num2 = float(input("Enter the second number (except for square, square root, sine, cosine, and tangent): "))
      except ValueError:
        print("Invalid input. Please enter numbers only.")
        continue

      # Perform calculation based on choice
      if choice == '1':
        result = add(num1, num2)
      elif choice == '2':
        result = subtract(num1, num2)
      elif choice == '3':
        result = multiply(num1, num2)
      elif choice == '4':
        result = divide(num1, num2)
      elif choice == '5':
        result = square(num1)
      elif choice == '6':
        result = square_root(num1)
      elif choice == '7':
        result = sine(num1)
      elif choice == '8':
        result = cosine(num1)
      elif choice == '9':
        result = tangent(num1)

      # Print the result
      print("Result:", result)
    else:
      print("Invalid choice. Please enter a number between 0 and 9.")

if __name__ == "__main__":
  main()
