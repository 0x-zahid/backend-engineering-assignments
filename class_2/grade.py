marks = int(input())

if marks < 0 or marks > 100:
    print(f"Invalid marks")
elif marks >= 80:
    print(f"Grade: A")
elif marks >= 70:
    print(f"Grade: B")
elif marks >= 60:
    print(f"Grade: C")
elif marks >= 50:
    print(f"Grade: D")
else:
    print(f"Grade: F")