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

def exponent(x, y):
  """Calculates x raised to the power of y."""
  return math.pow(x, y)

def factorial(x):
  """Calculates the factorial of a number."""
  if x < 0:
    return "Error: Factorial is not defined for negative numbers."
  elif x == 0:
    return 1
  else:
    result = 1
    for i in range(1, x + 1):
      result *= i
    return result

def sine(x):
  """Calculates the sine of an angle."""
  option = input("Enter 'd' for degrees or 'r' for radians: ")
  if option == 'd':
    return math.sin(math.radians(x))
  elif option == 'r':
    return math.sin(x)
  else:
    print("Invalid choice. Please enter 'd' or 'r'.")
    return None  # Handle invalid input gracefully

def cosine(x):
  """Calculates the cosine of an angle."""
  option = input("Enter 'd' for degrees or 'r' for radians: ")
  if option == 'd':
    return math.cos(math.radians(x))
  elif option == 'r':
    return math.cos(x)
  else:
    print("Invalid choice. Please enter 'd' or 'r'.")
    return None

def tangent(x):
  """Calculates the tangent of an angle (handles division by zero)."""
  if math.cos(math.radians(x)) == 0:
    return "Error: Cannot take tangent at 90 degrees or 270 degrees."
  else:
    return math.tan(math.radians(x))

# Memory variables
memory = None

def store_in_memory(result):
  """Stores the result in memory."""
  global memory
  memory = result

def recall_from_memory():
  """Recalls the stored result from memory."""
  global memory
  return memory

def clear_memory():
  """Clears the stored result from memory."""
  global memory
  memory = None

def main():
  """Main function for interactive calculator use."""
  print("Welcome to the Enhanced Calculator!")

  while True:
    print("\nAvailable operations:")
    print(" 1. Add")
    print(" 2. Subtract")
    print(" 3. Multiply")
    print(" 4. Divide")
    print(" 5. Square")
    print(" 6. Square Root")
    print(" 7. Exponent")
    print(" 8. Factorial")
    print(" 9. Sine (degrees/radians)")
    print(" 10. Cosine (degrees/radians)")
    print(" 11. Tangent (degrees/radians)")
    print(" 12. Store in Memory (M)")
    print(" 13. Recall from Memory (R)")
    print(" 14. Clear Memory (C)")
    print(" 0. Exit")

    choice = input("Enter your choice (0-14): ")

    if choice in ('0', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14'):
      if choice == '0':
        print("Exiting calculator.")
        break

      # Get numbers
      try:
        if choice in ('1', '2', '
