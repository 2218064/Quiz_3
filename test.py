students = [90, 45, 64, 9, 17, 29]
result=[]
for i in students:
    if i >= 71 :
        result.append("A")
    elif 71 > i >= 41 :
        result.append("B")
     elif 41 > i >= 11 :
        result.append("C")
     else :
        result.append("D")
print(result)

