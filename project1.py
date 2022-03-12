#task1
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list2 = []

def function(l):
    for i in l:
        if type(i) == list:
            function(i)
        else:
            list2.append(i)


function(list1)
print(list2)



#task2
list1 = [[1,'a',['cat'],2],[[[3]],'dog'],4,5]
list2 = []

def function(l):
    for i in l:
        if type(i) == list:
            function(i)
        else:
            list2.append(i)


function(list1)
print(list2)
    