file=open("sorted_list.txt",'w')
abc=[9,3,2,6,1,0]
print("Before Sorting:",abc)
file.write("Before Sorting:")
for i in abc:
    file.write(str(i))
    file.write(' ')
file.write('\n')
abc.sort(reverse=True)
print("After Sorting:",abc)
file.write("After Sorting:")
for i in abc:
    file.write(str(i))
    file.write(' ')
