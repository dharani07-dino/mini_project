# Student Grade Calculator

name = input("Enter student name: ")

mark1 = float(input("Enter mark for Subject 1: "))
mark2 = float(input("Enter mark for Subject 2: "))
mark3 = float(input("Enter mark for Subject 3: "))

total = mark1 + mark2 + mark3
average = total / 3

print("\n--- Student Result ---")
print("Name:", name)
print("Total:", total)
print("Average:", average)

if average >= 90:
    print("Grade: A")
elif average >= 80:
    print("Grade: B")
elif average >= 70:
    print("Grade: C")
elif average >= 60:
    print("Grade: D")
elif average >= 50:
    print("Grade: E")
else:
    print("Grade: F")
