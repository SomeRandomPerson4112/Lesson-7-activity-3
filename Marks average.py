print("Enter marks obtained in 5 subjects")
sub1=int(input())
sub2=int(input())
sub3=int(input())
sub4=int(input())
sub5=int(input())
total=sub1+sub2+sub3+sub4+sub5
avg=total/5
if avg>=91 and avg<=100:
    print("Your grade is A1")
elif avg>=81 and avg<=90:
    print("Your grade is A2")
elif avg>=71 and avg<=80:
    print("Your grade is B1")
elif avg>=61 and avg<=70:
    print("Your grade is B2")
elif avg>=51 and avg<=60:
    print("Your grade is C1")
elif avg>=41 and avg<=50:
    print("Your grade is C2")
elif avg>=31 and avg<=40:
    print("Your grade is D")
elif avg>=21 and avg<=30:
    print("Your grade is E1")
elif avg>=0 and avg<=20:
    print("Your grade is E2")
else:
    print("Invalid input")