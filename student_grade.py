m1=float(input("enter marks for sub1:"))
m2=float(input("enter marks for sub2:"))
m3=float(input("enter marks for sub3:"))
m4=float(input("enter marks for sub4:"))
m5=float(input("enter marks for sub5:"))
average=(m1+m2+m3+m4+m5)/5
if average >=90:
    grade='A'
elif average >=80:
    grade='B'
elif average >=75:
    grade='C'
elif average >=60:
    grade='D'
else:
    grade='Fail'
print("Average marks:",average)
print("Grade:",grade)
