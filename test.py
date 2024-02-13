from functools import reduce
list1 = range(1,21)
list2 = []
for i in list1:
    list2.append(i)
print (list2)

list2 = [x for x in list1]
print(list2)

list3 = map(lambda x: x, range(1,21))
print(list(list3))
      
list4 = filter(lambda x: x%2==0, range(1,21))
print(list(list4))

list5 = reduce(lambda x,y: x+y, list1, 0)
print(list5)
