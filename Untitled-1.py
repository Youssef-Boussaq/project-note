n1 = float(input("write your first note: "))
n2 = float(input("write your second note: "))
n3 = float(input("write your last note: "))
# user write the right note
while n1 > 20 or n1 < 0 :
   print("try again")
   n1 = float(input("write your first note: "))
while  n2 > 20 or n2 < 0:
   print("try again")
   n2 = float(input("write your second note: "))
while  n3 > 20 or n3 < 0:
    print("try again")
    n3= float(input("write your second note: "))
m = (n1 + n2 + n3)/3
if m >= 16 :
    print("Alright",m)
elif m < 16 and m >= 14:
    print("good",m)
elif m<14 and m>=12:
    print("pretty good",m)
elif m<12 and m>=10:
    print("passable",m)
else:
    print("insufficient",m)