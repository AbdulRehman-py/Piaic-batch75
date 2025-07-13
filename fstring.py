# prompt: generate a grading system for school which takes marks as an  input show grade according to the marks

def grading_system(marks):
  """
  This function takes marks as input and returns the corresponding grade.

  Args:
    marks: The marks obtained by the student.

  Returns:
    The grade corresponding to the marks.
  """
  if marks >= 90:
    grade = "A+"
  elif marks >= 80:
    grade = "A"
  elif marks >= 70:
    grade = "B"
  elif marks >= 60:
    grade = "C"
  elif marks >= 50:
    grade = "D"
  else:
    grade = "F"
  return grade

# Get marks as input from the user
while True:
  try:
    marks = float(input("Enter the marks: "))
    if 0 <= marks <= 100:
      break
    else:
      print("Marks must be between 0 and 100.")
  except ValueError:
    print("Invalid input. Please enter a number.")

# Determine the grade
grade = grading_system(marks)

# Print the grade
print(f"The grade for {marks} marks is: {grade}")
