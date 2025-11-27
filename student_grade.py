import sys

# Check if 5 subject marks are provided
if len(sys.argv) == 6:
    script_name = sys.argv[0]
    Eng = float(sys.argv[1])
    Math = float(sys.argv[2])
    Sci = float(sys.argv[3])
    Hindi = float(sys.argv[4])
    SS = float(sys.argv[5])
    print("User provided input values:")
else:
    script_name = sys.argv[0]
    Eng = 75
    Math = 80
    Sci = 70
    Hindi = 85
    SS = 90
    print("No input given - using default values:")
# Calculate average
average = (Eng + Math + Sci + Hindi + SS) / 5
# Grade calculation
if average >= 90:
    grade = "A"
elif average >= 75:
    grade = "B"
elif average >= 60:
    grade = "C"
elif average >= 50:
    grade = "D"
else:
    grade = "Fail"

# Display results
print("Script Name:", script_name)
print("Marks:", Eng,Math,Sci,Hindi,SS)
print("Average Marks:", round(average, 2))
print("Grade:", grade)
