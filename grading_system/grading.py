print("Enter Marks")
marks = int(input())

if 0 < marks < 33:
    print("Grade F")

elif 33 <= marks <= 40:
    print("Grade D")

elif 41 <= marks <= 50:
    print("Grade C")

elif 51 <= marks <= 60:
    print("Grade B")

elif 61 <= marks <= 70:
    print("Grade A-")

elif 71 <= marks <= 80:
    print("Grade A")

elif 81 <= marks <= 100:
    print("Grade A+")
else:
    print("Invalied")
#
# elif marks>34 and marks<40:
#     print("Grade D")
#
# elif marks>41 and marks<50:
#     print("Grade D")
#
# elif marks>51 and marks<60:
#     print("Grade D")
#
# elif marks>61 and marks<70:
#     print("Grade D")
#
# elif marks>71 and marks<80:
#     print("Grade D")
#
# elif marks>81 and marks<100:
#     print("Grade D")
#
#
