arr = []
x = int(input("Enter any intigers: "))
for i in range(1,x+1):
     a = int(input())
     if a > 100:
         arr.append("Over")
     else:
         arr.append(a)
     print(arr)
