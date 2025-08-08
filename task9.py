a={'John':88,'James':65,'ALice':72}
n=input("Enter the student's name:")
if n in a:
    print(n,"marks:",a[n])
else:
    print("Student not found.")
