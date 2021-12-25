lst = [11, 5, 8, 32, 15, 3, 20, 132, 21, 4, 555, 9, 20]
a = []
j=0
s=0
for i in lst:
    if i<30 and i>2 and i%3==0:
        a.append(i)
        del(lst[j])
        j+=1
    else:
        s+=i
        j+=1
print(f"Done: {a}\nSumma = {s}")
        
